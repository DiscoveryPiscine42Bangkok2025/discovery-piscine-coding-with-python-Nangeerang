def checkmate(board_string):
    """
    ฟังก์ชันหลักในการตรวจสอบว่า King อยู่ในสถานะ checkmate หรือไม่
    รับ board string และ print "Success" ถ้า King ถูกโจมตี, "Fail" ถ้าปลอดภัย
    """
    # แปลง board string ให้เป็น list ของ strings (แต่ละ row)
    board = board_string.strip().split('\n')
    # หาตำแหน่งของ King บนกระดาน
    king_pos = None
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:  # ออกจาก loop นอกถ้าเจอ King แล้ว
            break
    
    # ถ้าไม่เจอ King ให้ return Fail
    if not king_pos:
        print("Fail")
        return
    
    king_r, king_c = king_pos
    
    # ตรวจสอบทุกตำแหน่งบนกระดานหาตัวหมาก (P, R, B, Q)
    for r in range(len(board)):
        for c in range(len(board[r])):
            piece = board[r][c]
            
            # ตรวจสอบว่าตัวหมากแต่ละชนิดสามารถโจมตี King ได้หรือไม่
            if piece == 'P' and can_pawn_attack(r, c, king_r, king_c):
                print("Success")  # Pawn สามารถโจมตี King ได้
                return
            elif piece == 'R' and can_rook_attack(board, r, c, king_r, king_c):
                print("Success")  # Rook สามารถโจมตี King ได้
                return
            elif piece == 'B' and can_bishop_attack(board, r, c, king_r, king_c):
                print("Success")  # Bishop สามารถโจมตี King ได้
                return
            elif piece == 'Q' and can_queen_attack(board, r, c, king_r, king_c):
                print("Success")  # Queen สามารถโจมตี King ได้
                return
    
    # ถ้าไม่มีตัวหมากไหนโจมตี King ได้ แสดงว่าปลอดภัย
    print("Fail")

def can_pawn_attack(pawn_r, pawn_c, king_r, king_c):
    """
    ตรวจสอบว่า Pawn สามารถโจมตี King ได้หรือไม่
    Pawn โจมตีแบบทแยงขึ้นบน: ขึ้น 1 แถว, เลื่อน 1 คอลัมน์ซ้ายหรือขวา
    """
    # Pawn ต้องอยู่ 1 แถวด้านล่าง King (pawn_r - king_r == 1)
    # และ 1 คอลัมน์ห่างทแยง (ผลต่าง abs == 1)
    return pawn_r - king_r == 1 and abs(pawn_c - king_c) == 1

def can_rook_attack(board, rook_r, rook_c, king_r, king_c):
    """
    ตรวจสอบว่า Rook สามารถโจมตี King ได้หรือไม่
    Rook โจมตีแบบแนวนอนและแนวตั้งเป็นเส้นตรง
    """
    # Rook ต้องอยู่ในแถวเดียวกัน หรือ คอลัมน์เดียวกันกับ King
    if rook_r != king_r and rook_c != king_c:
        return False
    
    # ตรวจสอบว่าเส้นทางระหว่าง Rook และ King ว่าง (ไม่มีตัวหมากขวาง)
    if rook_r == king_r:  # แถวเดียวกัน - ตรวจเส้นทางแนวนอน
        start, end = min(rook_c, king_c), max(rook_c, king_c)
        for c in range(start + 1, end):  # ตรวจคอลัมน์ระหว่าง Rook และ King
            if board[rook_r][c] != '.':
                return False  # เส้นทางถูกขวาง
    else:  # คอลัมน์เดียวกัน - ตรวจเส้นทางแนวตั้ง
        start, end = min(rook_r, king_r), max(rook_r, king_r)
        for r in range(start + 1, end):  # ตรวจแถวระหว่าง Rook และ King
            if board[r][rook_c] != '.':
                return False  # เส้นทางถูกขวาง
    
    return True  # เส้นทางว่าง, Rook สามารถโจมตีได้

def can_bishop_attack(board, bishop_r, bishop_c, king_r, king_c):
    """
    ตรวจสอบว่า Bishop สามารถโจมตี King ได้หรือไม่
    Bishop โจมตีแบบทแยงในทิศทาง 4 ทิศทางทแยง
    """
    # Bishop ต้องอยู่บนเส้นทแยงจาก King
    # ผลต่างของแถว ต้องเท่ากับ ผลต่างของคอลัมน์ สำหรับการเคลื่อนที่ทแยง
    if abs(bishop_r - king_r) != abs(bishop_c - king_c):
        return False
    
    # ตรวจสอบว่าเส้นทางทแยงว่าง (ไม่มีตัวหมากขวาง)
    # คำนวณทิศทางการเดิน: +1 หรือ -1 สำหรับแต่ละแกน
    r_step = 1 if king_r > bishop_r else -1
    c_step = 1 if king_c > bishop_c else -1
    
    # เคลื่อนไปตามทแยงจาก Bishop ไปหา King
    r, c = bishop_r + r_step, bishop_c + c_step
    while r != king_r:  # หยุดเมื่อถึงตำแหน่ง King
        if board[r][c] != '.':
            return False  # เส้นทางถูกขวาง
        r += r_step
        c += c_step
    
    return True  # เส้นทางว่าง, Bishop สามารถโจมตีได้

def can_queen_attack(board, queen_r, queen_c, king_r, king_c):
    """
    ตรวจสอบว่า Queen สามารถโจมตี King ได้หรือไม่
    Queen รวมการเคลื่อนที่ของ Rook และ Bishop (แนวนอน, แนวตั้ง, และทแยง)
    """
    # Queen สามารถโจมตีได้เหมือน Rook หรือ Bishop
    return (can_rook_attack(board, queen_r, queen_c, king_r, king_c) or 
            can_bishop_attack(board, queen_r, queen_c, king_r, king_c))