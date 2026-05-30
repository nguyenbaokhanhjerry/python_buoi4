students = []
def classify_student(avg_score):
    if avg_score < 5:
        return "Yếu"
    elif avg_score < 7:
        return "Trung Bình"
    elif avg_score < 8:
        return "Khá"
    else:
        return "Giỏi"
def calculate_info(student):
    avg_score = round(
        (student["math_score"] +
        student["physics_score"] +
        student["chemistry_score"]) / 3, 2
    )
    student["avg_score"] = avg_score
    student["rank"] = classify_student(avg_score)
def display_students():
    if len(students) == 0:
        print("Danh sách sinh viên trống!")
        return
    print("DANH SÁCH SINH VIÊN")
    print("-" * 90)
    print(
        f"{'Mã SV':<10}"
        f"{'Tên':<25}"
        f"{'Toán':<10}"
        f"{'Lý':<10}"
        f"{'Hóa':<10}"
        f"{'Điểm TB':<10}"
        f"{'Xếp Loại':<15}"
    )
    print("-" * 90)
    for student in students:
        print(
            f"{student['id']:<10}"
            f"{student['name']:<25}"
            f"{student['math_score']:<10}"
            f"{student['physics_score']:<10}"
            f"{student['chemistry_score']:<10}"
            f"{student['avg_score']:<10}"
            f"{student['rank']:<15}"
        )
def add_student():
    student_id = input("Nhập mã sinh viên: ")
    for student in students:
        if student["id"] == student_id:
            print("Mã sinh viên đã tồn tại!")
            return
    name = input("Nhập tên sinh viên: ")
    math_score = float(input("Nhập điểm Toán: "))
    physics_score = float(input("Nhập điểm Lý: "))
    chemistry_score = float(input("Nhập điểm Hóa: "))
    if (
        math_score < 0 or math_score > 10 or
        physics_score < 0 or physics_score > 10 or
        chemistry_score < 0 or chemistry_score > 10
    ):
        print("Điểm phải nằm trong khoảng từ 0 đến 10!")
        return
    student = {
        "id": student_id,
        "name": name,
        "math_score": math_score,
        "physics_score": physics_score,
        "chemistry_score": chemistry_score
    }
    calculate_info(student)
    students.append(student)
    print("Thêm sinh viên thành công!")
def update_student():
    student_id = input("Nhập mã sinh viên cần cập nhật: ")
    for student in students:
        if student["id"] == student_id:
            student["math_score"] = float(
                input("Nhập điểm Toán mới: ")
            )
            student["physics_score"] = float(
                input("Nhập điểm Lý mới: ")
            )
            student["chemistry_score"] = float(
                input("Nhập điểm Hóa mới: ")
            )
            calculate_info(student)
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy sinh viên!")
def delete_student():
    student_id = input("Nhập mã sinh viên cần xóa: ")
    for student in students:
        if student["id"] == student_id:
            confirm = input(
                "Bạn có chắc muốn xóa? (y/n): "
            )
            if confirm.lower() == "y":
                students.remove(student)
                print("Xóa thành công!")
            else:
                print("Đã hủy xóa!")
            return
    print("Không tìm thấy sinh viên!")
def search_student():
    keyword = input(
        "Nhập mã sinh viên hoặc tên cần tìm: "
    ).lower()

    found = False

    for student in students:
        if (
            keyword in student["id"].lower()
            or keyword in student["name"].lower()
        ):
            print(student)
            found = True

    if not found:
        print("Không tìm thấy sinh viên!")
def sort_students():
    print("1. Điểm TB giảm dần")
    print("2. Tên tăng dần")
    choice = input("Chọn cách sắp xếp: ")
    if choice == "1":
        students.sort(
            key=lambda student: student["avg_score"],
            reverse=True
        )
    elif choice == "2":
        students.sort(
            key=lambda student: student["name"]
        )
    else:
        print("Lựa chọn không hợp lệ!")
        return
    print("Sắp xếp thành công!")
def statistics():
    excellent = 0
    good = 0
    average = 0
    weak = 0
    for student in students:
        if student["rank"] == "Giỏi":
            excellent += 1
        elif student["rank"] == "Khá":
            good += 1
        elif student["rank"] == "Trung Bình":
            average += 1
        else:
            weak += 1
    print("THỐNG KÊ HỌC LỰC")
    print("Giỏi:", excellent)
    print("Khá:", good)
    print("Trung Bình:", average)
    print("Yếu:", weak)
def top_bottom_students():
    if len(students) == 0:
        print("Danh sách sinh viên trống!")
        return
    max_score = max(
        student["avg_score"]
        for student in students
    )
    min_score = min(
        student["avg_score"]
        for student in students
    )
    print("SINH VIÊN CÓ ĐIỂM TB CAO NHẤT")
    for student in students:
        if student["avg_score"] == max_score:
            print(student)
    print("SINH VIÊN CÓ ĐIỂM TB THẤP NHẤT")
    for student in students:
        if student["avg_score"] == min_score:
            print(student)
def classify_all_students():
    for student in students:
        calculate_info(student)
    print("Đã cập nhật xếp loại học lực!")
while True:
    print("========== QUẢN LÝ SINH VIÊN ==========")
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm mới sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Sắp xếp danh sách sinh viên")
    print("7. Thống kê điểm TB")
    print("8. Liệt kê sinh viên điểm cao nhất/thấp nhất")
    print("9. Phân loại học lực sinh viên")
    print("0. Thoát")
    choice = int(input("Nhập lựa chọn: "))
    match choice:
        case 1:
            display_students()
        case 2:
            add_student()
        case 3:
            update_student()
        case 4:
            delete_student()
        case 5:
            search_student()
        case 6:
            sort_students()
        case 7:
            statistics()
        case 8:
            top_bottom_students()
        case 9:
            classify_all_students()
        case 0:
            print("Đã thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
