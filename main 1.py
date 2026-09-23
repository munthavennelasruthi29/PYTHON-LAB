# --- main.py (using the package) ---
from sams_package import Student, Faculty, Course, compile_result

if __name__ == "__main__":
    s = Student("SAMS24CS014", "Ananya Rao")
    result = compile_result(s, [88, 76, 92])
    print("=== SAMS Modular Package Test ===")
    print(f"{s.name} ({s.roll_no}) -> Total: {result['total']}, Average: {result['average']}")