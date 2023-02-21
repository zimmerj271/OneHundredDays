from type_test import TypeTest, TypeTestGUI


def main():
    type_test = TypeTest(50)
    window = TypeTestGUI(type_test)
    window.mainloop()


if __name__ == '__main__':
    main()
