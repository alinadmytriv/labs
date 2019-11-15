import re

"""All Lessons"""
def lesson1():
    # exercise 1
    print("---l1---\nMatch\tabcdefg\nMatch\tabcde\nMatch\tabc")
    # pattern0 = input(r"Enter raw string that match _all_ text: ")
    pattern0 = r"abc"
    if re.match(pattern0, "abcdefg") \
            and re.match(pattern0, "abcde") \
            and re.match(pattern0, "abc"):
        print("Match")
    else:
        print("No match")

def lesson1_2():
    # exercise 1.5
    print("\n---l1_2---\nMatch\tabc123xyz\nMatch\tdefine \"123\"\nMatch\tvar g = 123;")
    # pattern1 = input(r"Enter raw string that match _all_ text: ")
    pattern1 = r"([\w\D\"]+)[1-3]([\D\";]+)"
    if re.match(pattern1, "abc123xyz") \
            and re.match(pattern1, "define \"123\"") \
            and re.match(pattern1, "var g = 123;"):
        print("Match")
    else:
        print("No match")

def lesson2():
    # exercise 2
    print("\n---l2---\nMatch\tcat.\nMatch\t896.\nMatch\t?=+.\nSkip\tabc1")
    # pattern2 = input(r"Enter raw string that match _all_ text: ")
    pattern2 = r".*\.$"
    if re.match(pattern2, "cat.") \
            and re.match(pattern2, "896.") \
            and re.match(pattern2, "?=+."):
        print("Match")
    else:
        print("No match")

def lesson3():
    # exercise 3
    print("\n---l3---\nMatch\tcan\nMatch\tman\nSkip\tdan\nSkip\tran")
    # pattern3 = input(r"Enter raw string that match _all_ text: ")
    pattern3 = r"[cmf]an"
    # pattern3 = r"[^drp]an"
    if re.match(pattern3, "can") \
            and re.match(pattern3, "man"):
        print("Match")
    else:
        print("No match")

def lesson4():
    # exercise 4
    print("\n---l4---\nMatch\thog\nMatch\tdog\nSkip\tbog")
    # pattern4 = input(r"Enter raw string that match _all_ text: ")
    pattern4 = r"[hd]og"
    # pattern4 = r"[^b]og"
    if re.match(pattern4, "hog") \
            and re.match(pattern4, "dog"):
        print("Match")
    else:
        print("No match")

def lesson5():
    # exercise 5
    print("\n---l5---\nMatch\tAna\nMatch\tBob\nMatch\tCpc\nSkip\taax\nSkip\tbby\nSkip\tccz")
    #pattern5 = input(r"Enter raw string that match _all_ text: ")
    pattern5 = r"[A-Z][n-p][a-c]"
    if re.match(pattern5, "Ana") \
            and re.match(pattern5, "Bob") \
            and re.match(pattern5, "Cpc"):
        print("Match")
    else:
        print("No match")

def lesson6():
    # exercise 6
    print("\n---l6---\nMatch\twazzzzzup\nMatch\twazzzup\nSkip\twazup")
    #pattern6 = input(r"Enter raw string that match _all_ text: ")
    pattern6 = r"waz{3,5}up"
    if re.match(pattern6, "wazzzzzup") \
            and re.match(pattern6, "wazzzup"):
        print("Match")
    else:
        print("No match")

def lesson7():
    # exercise 7
    print("\n---l7---\nMatch\taabbbbc\nMatch\taacc\nSkip\ta")
    #pattern7 = input(r"Enter raw string that match _all_ text: ")
    pattern7 = r"^a+b*c+$"
    if re.match(pattern7, "aabbbbc")\
            and re.match(pattern7, "aacc"):
        print("Match")
    else:
        print("No match")

def lesson8():
    # exercise 8
    print("\n---l8---\nMatch\t1 file found?\nMatch\t24 files found?\nSkip\tNo files found?")
    #pattern8 = input(r"Enter raw string that match _all_ text: ")
    pattern8 = r"\d+ files? found\?"
    if re.match(pattern8, "1 file found?") \
            and re.match(pattern8, "24 files found?"):
        print("Match")
    else:
        print("No match")

def lesson9():
    # exercise 9
    print("\n---l9---\nMatch\t1.  abc\nMatch\t2.   abc\nSkip\t3.abc")
    #pattern9 = input(r"Enter raw string that match _all_ text: ")
    pattern9 = r"\d\.\s+abc"
    if re.match(pattern9, "1.  abc") \
            and re.match(pattern9, "2.   abc"):
        print("Match")
    else:
        print("No match")

def lesson10():
    # exercise 10
    print("\n---l10---\nMatch\tMission: successful\nSkip\tNext Mission: successful upon capture of target")
    #pattern10 = input(r"Enter raw string that match _all_ text: ")
    pattern10 = r"^Mission: successful$"
    if re.match(pattern10, "Mission: successful"):
        print("Match")
    else:
        print("No match")

def lesson11():
    # exercise 11
    print("\n---l11---\nCapture\tfile_record_transcript.pdf\nCapture\tfile_07241999.pdf\nSkip\ttestfile_fake.pdf.tmp")
    #pattern11 = input(r"Enter raw string that match _all_ text: ")
    pattern11 = r"^(file.+)\.pdf$"
    if re.match(pattern11, "file_record_transcript.pdf") \
            and re.match(pattern11, "file_07241999.pdf"):
        print("Match")
    else:
        print("No match")

def lesson12():
    # exercise 12
    print("\n---l12---\nCapture\tJan 1987\tJan 1987 1987")
    #pattern12 = input(r"Enter raw string that match _all_ text: ")
    pattern12 = r"(... (\d+))"
    if re.match(pattern12, "Jan 1987 1987"):
        print("Match")
    else:
        print("No match")

def lesson13():
    # exercise 13
    print("\n---l13---\nCapture\t1280x720\t1280 720\nCapture\t1920x1600\t1920 1600")
    #pattern13 = input(r"Enter raw string that match _all_ text: ")
    pattern13 = r"(\d+)x(\d+)"
    if re.match(pattern13, "1280x720") \
            and re.match(pattern13, "1920x1600"):
        print("Match")
    else:
        print("No match")

def lesson14():
    # exercise 14
    print("\n---l14---\nMatch\tI love cats\nMatch\tI love dogs\nSkip\tI love cogs")
    #pattern14 = input(r"Enter raw string that match _all_ text: ")
    pattern14 = r"I love (cats|dogs)"
    if re.match(pattern14, "I love cats") \
            and re.match(pattern14, "I love dogs"):
        print("Match")
    else:
        print("No match")

def lesson15():
    # exercise 15
    print("\n---l15---\nMatch\tThe quick brown fox jumps over the lazy dog.\nMatch\tThe FCC had to censor the network for saying &$#*@!.")
    #pattern15 = input(r"Enter raw string that match _all_ text: ")
    pattern15 = r".*"
    if re.match(pattern15, "The quick brown fox jumps over the lazy dog.") \
            and re.match(pattern15, "The FCC had to censor the network for saying &$#*@!."):
        print("Match")
    else:
        print("No match")

def all_lessons():
    """All Lessons"""
    lesson1()
    lesson1_2()
    lesson2()
    lesson3()
    lesson4()
    lesson5()
    lesson6()
    lesson7()
    lesson8()
    lesson9()
    lesson10()
    lesson11()
    lesson12()
    lesson13()
    lesson14()
    lesson15()

"""Practice Problems"""
def problem1():
    # exercise 1
    print("\n---p1---\nMatch\t3.14529\nMatch\t128\nMatch\t1.9e10\nMatch\t123,340.00\nSkip\t720p")
    #pattern1_1 = input(r"Enter raw string that match _all_ text: ")
    pattern1_1 = r"^-?\d+(,\d+)*(\.\d+(e\d+)?)?$"
    if re.match(pattern1_1, "3.14529")\
            and re.match(pattern1_1, "128")\
            and re.match(pattern1_1, "1.9e10")\
            and re.match(pattern1_1, "123,340.00"):
        print("Match")
    else:
        print("No match")

def problem2():
    # exercise 2
    print("\n---p2---\nCapture\t415-555-1234\t415\nCapture\t(416)555-3456\t416\nCapture\t202 555 4567\t202\nCapture\t4035555678\t403\nCapture\t1 416 555 9292\t416")
    #pattern2_2 = input(r"Enter raw string that match _all_ text: ")
    pattern2_2 = r"1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}"
    if re.match(pattern2_2, "415-555-1234")\
            and re.match(pattern2_2, "(416)555-3456")\
            and re.match(pattern2_2, "202 555 4567")\
            and re.match(pattern2_2, "4035555678")\
            and re.match(pattern2_2, "1 416 555 9292"):
        print("Match")
    else:
        print("No match")

def problem3():
    # exercise 3
    print("\n---p3---\nCapture\ttom@hogwarts.com\nCapture\ttom.riddle@hogwarts.com\nCapture\ttom.riddle+regexone@hogwarts.com")
    #pattern3_3 = input(r"Enter raw string that match _all_ text: ")
    pattern3_3 = r"^([\w\.]*)"
    if re.match(pattern3_3, "tom@hogwarts.com")\
            and re.match(pattern3_3, "tom.riddle@hogwarts.com")\
            and re.match(pattern3_3, "tom.riddle+regexone@hogwarts.com"):
        print("Match")
    else:
        print("No match")

def problem4():
    # exercise 4
    print("\n---p4---\nCapture\timg0912.jpg\nCapture\tfavicon.gif\nCapture\tupdated_img0912.png\nSkip\tdocumentation.html\nSkip\t.bash_profile")
    #pattern4_4 = input(r"Enter raw string that match _all_ text: ")
    pattern4_4 = r"^(\w+).(jpg|png|gif)$"
    if re.match(pattern4_4, "img0912.jpg")\
            and re.match(pattern4_4, "favicon.gif")\
            and re.match(pattern4_4, "updated_img0912.png"):
        print("Match")
    else:
        print("No match")

def problem5():
    # exercise 5
    print("\n---p5---\nCapture\t				The quick brown fox...\nCapture\t   jumps over the lazy dog.")
    #pattern5_5 = input(r"Enter raw string that match _all_ text: ")
    pattern5_5 = r"^\s*(.*)\s*$"
    if re.match(pattern5_5, "				The quick brown fox...")\
            and re.match(pattern5_5, "   jumps over the lazy dog."):
        print("Match")
    else:
        print("No match")

def problem6():
    # exercise 6
    print("\n---p6---\nSkip\tW/dalvikvm( 1553): threadid=1: uncaught exception\nCapture\tE/( 1553):   at widget.List.makeView(ListView.java:1727)	")
    #pattern6_6 = input(r"Enter raw string that match _all_ text: ")
    pattern6_6 = r"E/\( \d+\):\s+\D+\.(\w+)\((\w+.\w+):(\d+)\)"
    if re.match(pattern6_6, "E/( 1553):   at widget.List.makeView(ListView.java:1727)	"):
        print("Match")
    else:
        print("No match")

def problem7():
    # exercise 7
    print("\n---p7---\nCapture\tftp://file_server.com:21/top_secret/life_changing_plans.pdf\tftp file_server.com 21\nCapture\tfile://localhost:4040/zip_file\tfile localhost 4040")
    #pattern7_7 = input(r"Enter raw string that match _all_ text: ")
    pattern7_7 = r"(\w+)://(\w+-?(\w+)?(\.com)?)[:/]?(\d+)?([/\w+]+)?([\.\w+]+)?"
    if re.match(pattern7_7, "ftp://file_server.com:21/top_secret/life_changing_plans.pdf")\
            and re.match(pattern7_7, "file://localhost:4040/zip_file"):
        print("Match")
    else:
        print("No match")

def practice_problems():
    """Practice Problems"""
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
    problem7()


def main():
    all_lessons()
    practice_problems()

if __name__ == '__main__':
    main()