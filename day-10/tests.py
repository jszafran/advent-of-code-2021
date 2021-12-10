import unittest

from solution import complete_line, get_illegal_char_for_line


class TestSuite(unittest.TestCase):
    def test_find_illegal_char(self):
        self.assertEqual("}", get_illegal_char_for_line("{([(<{}[<>[]}>{[]{[(<()>"))
        self.assertEqual(")", get_illegal_char_for_line("[[<[([]))<([[{}[[()]]]"))
        self.assertEqual("]", get_illegal_char_for_line("[{[{({}]{}}([{[{{{}}([]"))
        self.assertEqual(")", get_illegal_char_for_line("[<(<(<(<{}))><([]([]()"))
        self.assertEqual(">", get_illegal_char_for_line("<{([([[(<>()){}]>(<<{{"))
        self.assertIsNone(get_illegal_char_for_line("[]"))
        self.assertIsNone(get_illegal_char_for_line("()"))
        self.assertIsNone(get_illegal_char_for_line("([])"))
        self.assertIsNone(get_illegal_char_for_line("{()()()}"))
        self.assertIsNone(get_illegal_char_for_line("<([{}])>"))
        self.assertIsNone(get_illegal_char_for_line("[<>({}){}[([])<>]]"))
        self.assertIsNone(get_illegal_char_for_line("(((((((((())))))))))"))

    def test_complete_line(self):
        self.assertEqual("}}]])})]", complete_line("[({(<(())[]>[[{[]{<()<>>"))
        self.assertEqual(")}>]})", complete_line("[(()[<>])]({[<{<<[]>>("))
        self.assertEqual("}}>}>))))", complete_line("(((({<>}<{<{<>}{[]{[]{}"))
        self.assertEqual("]]}}]}]}>", complete_line("{<[[]]>}<{[{[{[]{()[[[]"))
        self.assertEqual("])}>", complete_line("<{([{{}}[<[[[<>{}]]]>[]]"))
