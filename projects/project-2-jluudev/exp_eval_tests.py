# Start of unittest - add to completely test functions in exp_eval!

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):

    def test_postfix_eval_01a(self) -> None:
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01b(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self) -> None:
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)

    def test_postfix_eval_02(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()  # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03a(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()  # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self) -> None:
        try:
            postfix_eval("")
            self.fail()  # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()  # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_infix_to_postfix_01a(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")

    def test_infix_to_postfix_01b(self) -> None:
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self) -> None:
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self) -> None:
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self) -> None:
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self) -> None:
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_prefix_to_postfix(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_postfix_eval(self) -> None:
        self.assertEqual(postfix_eval("2 3 * 4 5 * +"), 26)
        self.assertEqual(postfix_eval("2 3 - 4 + 5 6 * -"), -27)
        self.assertEqual(postfix_eval("2 3 - 4 + 5 6 7 * + *"), 141)
        self.assertEqual(postfix_eval("2 2 **"), 4)
        self.assertEqual(postfix_eval("16 2 4 ** / 4 3 * + 6 2 * -"), 1)
        self.assertEqual(postfix_eval("2 2 2 << **"), 256)
        self.assertEqual(postfix_eval("2 2 ** 2 <<"), 16)
        self.assertEqual(postfix_eval("2 2 ** 2 >>"), 1)
        self.assertEqual(postfix_eval("2 2 ** 2 ** 2 /"), 8)
        self.assertEqual(postfix_eval("16 3 >> 2 **"), 4)
        self.assertEqual(postfix_eval("16 0 >> 1 /"), 16)
        self.assertEqual(postfix_eval("6"), 6)
        self.assertEqual(postfix_eval("2 3 2 ** **"), 512)
        self.assertEqual(postfix_eval(infix_to_postfix("2 ** 3 ** 2")), 512)
        self.assertEqual(postfix_eval(infix_to_postfix("2 ** 2 ** 3 ** 0")), 4)
        self.assertEqual(postfix_eval(infix_to_postfix("2 << 2 ** 3")), 512)
        self.assertEqual(postfix_eval(infix_to_postfix("-2 * -2")), 4)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("-2 ** -2")), 0.25)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("-2 ** 2")), 4)
        self.assertEqual(postfix_eval(infix_to_postfix("-2 ** 3")), -8)

        with self.assertRaises(PostfixFormatException):
            postfix_eval("6..66 6... +")

        with self.assertRaises(PostfixFormatException):
            postfix_eval("16 -1 >>")

        with self.assertRaises(PostfixFormatException):
            postfix_eval("16 -2 <<")

        with self.assertRaises(PostfixFormatException):
            postfix_eval("16.2 5.0 >>")

        with self.assertRaises(PostfixFormatException):
            postfix_eval("16.5 3 <<")

        with self.assertRaises(PostfixFormatException):
            postfix_eval("blah")

        with self.assertRaises(PostfixFormatException):
            postfix_eval("9 /")

        with self.assertRaises(ValueError):
            postfix_eval("9 0 /")

    def test_infix_to_postfix_a(self) -> None:
        self.assertEqual(infix_to_postfix("1 + 2 + 3 + 4"), "1 2 + 3 + 4 +")
        self.assertEqual(infix_to_postfix("1 * 2 + 3 * 4"), "1 2 * 3 4 * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * ( 3 + 4 )"), "1 2 + 3 4 + *")
        self.assertEqual(infix_to_postfix("1 + 2 * 3 + 4"), "1 2 3 * + 4 +")
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"), "2 3 2 ** **")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

        try:
            infix_to_postfix("")
            self.fail()  # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")


    def test_infix_to_postfix_b(self) -> None:
        try:
            infix_to_postfix("blah B C D * / 0 9")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")


    def test_prefix_to_postfix_a(self) -> None:
        self.assertEqual(prefix_to_postfix("+ + + 1 2 3 4"), "1 2 + 3 + 4 +")
        self.assertEqual(prefix_to_postfix("** ** ** 1 2 3 4"), "1 2 ** 3 ** 4 **")
        self.assertEqual(prefix_to_postfix("+ + 1 * 2 3 4"), "1 2 3 * + 4 +")
        self.assertEqual(prefix_to_postfix("* + 1 2 + 3 4"), "1 2 + 3 4 + *")
        self.assertEqual(prefix_to_postfix("67"), "67")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

        try:
            prefix_to_postfix("")
            self.fail()  # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")


    def test_prefix_to_postfix_b(self) -> None:
        try:
            prefix_to_postfix("A B C D * / 0 9")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")


    def test_calc(self) -> None:
        with self.assertRaises(PostfixFormatException):
            calc(1, 2, "%")
        with self.assertRaises(ValueError):
            calc(0, 1, "/")

if __name__ == "__main__":
    unittest.main()
