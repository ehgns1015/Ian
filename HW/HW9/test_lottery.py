"""
Lottery System - Automated Grading Test
========================================
Run this file to test and grade the lottery project.

Usage:
    python test_lottery.py

Total Points: 100
"""

import unittest
import sys
import io
from contextlib import redirect_stdout
from unittest.mock import patch

# ============================================================
# GRADING CONFIGURATION
# ============================================================

POINTS = {
    'constants': 5,
    'validator': 15,
    'lottery_ticket': 15,
    'lottery_machine': 20,
    'player': 15,
    'display': 10,
    'main': 10,
    'srp': 5,
    'style': 5,
}

# Store test results
results = {
    'constants': {'passed': 0, 'total': 0, 'points': 0},
    'validator': {'passed': 0, 'total': 0, 'points': 0},
    'lottery_ticket': {'passed': 0, 'total': 0, 'points': 0},
    'lottery_machine': {'passed': 0, 'total': 0, 'points': 0},
    'player': {'passed': 0, 'total': 0, 'points': 0},
    'display': {'passed': 0, 'total': 0, 'points': 0},
    'main': {'passed': 0, 'total': 0, 'points': 0},
    'srp': {'passed': 0, 'total': 0, 'points': 0},
    'style': {'passed': 0, 'total': 0, 'points': 0},
}


# ============================================================
# TEST: constants.py (5 points)
# ============================================================

class TestConstants(unittest.TestCase):
    """Test constants.py - 5 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'constants'
        results[cls.module_name]['total'] = 5
    
    def test_01_import_constants(self):
        """constants.py can be imported"""
        try:
            import constants
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import constants.py")
    
    def test_02_ticket_price_exists(self):
        """TICKET_PRICE constant exists and is 2"""
        import constants
        self.assertTrue(hasattr(constants, 'TICKET_PRICE'))
        self.assertEqual(constants.TICKET_PRICE, 2)
    
    def test_03_white_ball_constants(self):
        """WHITE_BALL constants exist with correct values"""
        import constants
        self.assertTrue(hasattr(constants, 'WHITE_BALL_MIN'))
        self.assertTrue(hasattr(constants, 'WHITE_BALL_MAX'))
        self.assertTrue(hasattr(constants, 'WHITE_BALL_COUNT'))
        self.assertEqual(constants.WHITE_BALL_MIN, 1)
        self.assertEqual(constants.WHITE_BALL_MAX, 69)
        self.assertEqual(constants.WHITE_BALL_COUNT, 5)
    
    def test_04_power_ball_constants(self):
        """POWER_BALL constants exist with correct values"""
        import constants
        self.assertTrue(hasattr(constants, 'POWER_BALL_MIN'))
        self.assertTrue(hasattr(constants, 'POWER_BALL_MAX'))
        self.assertEqual(constants.POWER_BALL_MIN, 1)
        self.assertEqual(constants.POWER_BALL_MAX, 26)
    
    def test_05_no_hardcoded_values(self):
        """Constants file contains expected constant names"""
        import constants
        expected = ['TICKET_PRICE', 'WHITE_BALL_MIN', 'WHITE_BALL_MAX', 
                    'WHITE_BALL_COUNT', 'POWER_BALL_MIN', 'POWER_BALL_MAX']
        for const in expected:
            self.assertTrue(hasattr(constants, const), f"Missing constant: {const}")


# ============================================================
# TEST: validator.py (15 points)
# ============================================================

class TestValidator(unittest.TestCase):
    """Test validator.py - 15 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'validator'
        results[cls.module_name]['total'] = 10
    
    def setUp(self):
        from validator import Validator
        self.validator = Validator()
    
    def test_01_import_validator(self):
        """validator.py can be imported"""
        try:
            from validator import Validator
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import Validator from validator.py")
    
    def test_02_validator_init(self):
        """Validator can be instantiated"""
        from validator import Validator
        v = Validator()
        self.assertIsNotNone(v)
    
    def test_03_validate_white_balls_valid(self):
        """validate_white_balls accepts valid input"""
        valid_balls = [1, 15, 30, 45, 69]
        result = self.validator.validate_white_balls(valid_balls)
        self.assertTrue(result)
    
    def test_04_validate_white_balls_invalid_count(self):
        """validate_white_balls rejects wrong count"""
        too_few = [1, 2, 3, 4]
        too_many = [1, 2, 3, 4, 5, 6]
        self.assertFalse(self.validator.validate_white_balls(too_few))
        self.assertFalse(self.validator.validate_white_balls(too_many))
    
    def test_05_validate_white_balls_duplicates(self):
        """validate_white_balls rejects duplicates"""
        duplicates = [1, 1, 2, 3, 4]
        self.assertFalse(self.validator.validate_white_balls(duplicates))
    
    def test_06_validate_white_balls_out_of_range(self):
        """validate_white_balls rejects out of range numbers"""
        too_low = [0, 1, 2, 3, 4]
        too_high = [1, 2, 3, 4, 70]
        self.assertFalse(self.validator.validate_white_balls(too_low))
        self.assertFalse(self.validator.validate_white_balls(too_high))
    
    def test_07_validate_power_ball_valid(self):
        """validate_power_ball accepts valid input"""
        self.assertTrue(self.validator.validate_power_ball(1))
        self.assertTrue(self.validator.validate_power_ball(13))
        self.assertTrue(self.validator.validate_power_ball(26))
    
    def test_08_validate_power_ball_invalid(self):
        """validate_power_ball rejects invalid input"""
        self.assertFalse(self.validator.validate_power_ball(0))
        self.assertFalse(self.validator.validate_power_ball(27))
        self.assertFalse(self.validator.validate_power_ball(-1))
    
    def test_09_validate_ticket_count(self):
        """validate_ticket_count works correctly"""
        self.assertTrue(self.validator.validate_ticket_count(1))
        self.assertTrue(self.validator.validate_ticket_count(10))
        self.assertFalse(self.validator.validate_ticket_count(0))
        self.assertFalse(self.validator.validate_ticket_count(-1))
    
    def test_10_validate_balance(self):
        """validate_balance works correctly"""
        self.assertTrue(self.validator.validate_balance(10, 5))
        self.assertTrue(self.validator.validate_balance(10, 10))
        self.assertFalse(self.validator.validate_balance(5, 10))


# ============================================================
# TEST: lottery_ticket.py (15 points)
# ============================================================

class TestLotteryTicket(unittest.TestCase):
    """Test lottery_ticket.py - 15 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'lottery_ticket'
        results[cls.module_name]['total'] = 8
    
    def test_01_import_lottery_ticket(self):
        """lottery_ticket.py can be imported"""
        try:
            from lottery_ticket import LotteryTicket
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import LotteryTicket from lottery_ticket.py")
    
    def test_02_ticket_init(self):
        """LotteryTicket can be instantiated"""
        from lottery_ticket import LotteryTicket
        ticket = LotteryTicket([1, 2, 3, 4, 5], 10)
        self.assertIsNotNone(ticket)
    
    def test_03_ticket_stores_white_balls(self):
        """LotteryTicket stores white_balls correctly"""
        from lottery_ticket import LotteryTicket
        balls = [5, 10, 15, 20, 25]
        ticket = LotteryTicket(balls, 10)
        stored = ticket.get_white_balls()
        self.assertEqual(sorted(stored), sorted(balls))
    
    def test_04_ticket_stores_power_ball(self):
        """LotteryTicket stores power_ball correctly"""
        from lottery_ticket import LotteryTicket
        ticket = LotteryTicket([1, 2, 3, 4, 5], 15)
        self.assertEqual(ticket.get_power_ball(), 15)
    
    def test_05_ticket_sorts_white_balls(self):
        """LotteryTicket sorts white_balls"""
        from lottery_ticket import LotteryTicket
        balls = [25, 5, 15, 10, 20]
        ticket = LotteryTicket(balls, 10)
        stored = ticket.get_white_balls()
        self.assertEqual(stored, sorted(balls))
    
    def test_06_ticket_str_method(self):
        """LotteryTicket __str__ returns formatted string"""
        from lottery_ticket import LotteryTicket
        ticket = LotteryTicket([5, 10, 15, 20, 25], 7)
        string = str(ticket)
        # Check that it contains the numbers in some format
        self.assertIn('05', string)
        self.assertIn('07', string)
        self.assertTrue('PB' in string or 'pb' in string.lower() or '|' in string)
    
    def test_07_get_white_balls_method(self):
        """get_white_balls method exists and works"""
        from lottery_ticket import LotteryTicket
        ticket = LotteryTicket([1, 2, 3, 4, 5], 10)
        self.assertTrue(hasattr(ticket, 'get_white_balls'))
        self.assertIsInstance(ticket.get_white_balls(), list)
    
    def test_08_get_power_ball_method(self):
        """get_power_ball method exists and works"""
        from lottery_ticket import LotteryTicket
        ticket = LotteryTicket([1, 2, 3, 4, 5], 10)
        self.assertTrue(hasattr(ticket, 'get_power_ball'))
        self.assertIsInstance(ticket.get_power_ball(), int)


# ============================================================
# TEST: lottery_machine.py (20 points)
# ============================================================

class TestLotteryMachine(unittest.TestCase):
    """Test lottery_machine.py - 20 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'lottery_machine'
        results[cls.module_name]['total'] = 12
    
    def setUp(self):
        from lottery_machine import LotteryMachine
        self.machine = LotteryMachine()
    
    def test_01_import_lottery_machine(self):
        """lottery_machine.py can be imported"""
        try:
            from lottery_machine import LotteryMachine
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import LotteryMachine from lottery_machine.py")
    
    def test_02_machine_init(self):
        """LotteryMachine can be instantiated"""
        from lottery_machine import LotteryMachine
        machine = LotteryMachine()
        self.assertIsNotNone(machine)
    
    def test_03_generate_random_ticket(self):
        """generate_random_ticket returns a LotteryTicket"""
        from lottery_ticket import LotteryTicket
        ticket = self.machine.generate_random_ticket()
        self.assertIsInstance(ticket, LotteryTicket)
    
    def test_04_random_ticket_valid_white_balls(self):
        """Random ticket has 5 unique white balls in range 1-69"""
        ticket = self.machine.generate_random_ticket()
        balls = ticket.get_white_balls()
        self.assertEqual(len(balls), 5)
        self.assertEqual(len(set(balls)), 5)  # unique
        for ball in balls:
            self.assertGreaterEqual(ball, 1)
            self.assertLessEqual(ball, 69)
    
    def test_05_random_ticket_valid_power_ball(self):
        """Random ticket has power ball in range 1-26"""
        ticket = self.machine.generate_random_ticket()
        pb = ticket.get_power_ball()
        self.assertGreaterEqual(pb, 1)
        self.assertLessEqual(pb, 26)
    
    def test_06_create_manual_ticket(self):
        """create_manual_ticket creates ticket with given numbers"""
        from lottery_ticket import LotteryTicket
        ticket = self.machine.create_manual_ticket([1, 2, 3, 4, 5], 10)
        self.assertIsInstance(ticket, LotteryTicket)
        self.assertEqual(sorted(ticket.get_white_balls()), [1, 2, 3, 4, 5])
        self.assertEqual(ticket.get_power_ball(), 10)
    
    def test_07_draw_winning_numbers(self):
        """draw_winning_numbers generates and stores winning ticket"""
        self.machine.draw_winning_numbers()
        winning = self.machine.get_winning_ticket()
        self.assertIsNotNone(winning)
    
    def test_08_get_winning_ticket_before_draw(self):
        """get_winning_ticket returns None before draw"""
        from lottery_machine import LotteryMachine
        new_machine = LotteryMachine()
        self.assertIsNone(new_machine.get_winning_ticket())
    
    def test_09_check_ticket_no_match(self):
        """check_ticket returns correct result for no matches"""
        self.machine.draw_winning_numbers()
        winning = self.machine.get_winning_ticket()
        
        # Create ticket with completely different numbers
        w_balls = winning.get_white_balls()
        w_pb = winning.get_power_ball()
        
        # Generate non-matching numbers
        diff_balls = []
        for i in range(1, 70):
            if i not in w_balls:
                diff_balls.append(i)
                if len(diff_balls) == 5:
                    break
        diff_pb = 1 if w_pb != 1 else 2
        
        ticket = self.machine.create_manual_ticket(diff_balls, diff_pb)
        result = self.machine.check_ticket(ticket)
        
        self.assertIn('white_matches', result)
        self.assertIn('power_match', result)
        self.assertIn('is_jackpot', result)
        self.assertEqual(result['white_matches'], 0)
        self.assertFalse(result['power_match'])
        self.assertFalse(result['is_jackpot'])
    
    def test_10_check_ticket_partial_match(self):
        """check_ticket returns correct result for partial matches"""
        self.machine.draw_winning_numbers()
        winning = self.machine.get_winning_ticket()
        
        w_balls = winning.get_white_balls()
        w_pb = winning.get_power_ball()
        
        # Match 2 white balls
        partial_balls = w_balls[:2]
        for i in range(1, 70):
            if i not in w_balls and len(partial_balls) < 5:
                partial_balls.append(i)
        
        ticket = self.machine.create_manual_ticket(partial_balls, w_pb)
        result = self.machine.check_ticket(ticket)
        
        self.assertEqual(result['white_matches'], 2)
        self.assertTrue(result['power_match'])
        self.assertFalse(result['is_jackpot'])
    
    def test_11_check_ticket_jackpot(self):
        """check_ticket returns jackpot for all matches"""
        self.machine.draw_winning_numbers()
        winning = self.machine.get_winning_ticket()
        
        # Create identical ticket
        ticket = self.machine.create_manual_ticket(
            winning.get_white_balls(), 
            winning.get_power_ball()
        )
        result = self.machine.check_ticket(ticket)
        
        self.assertEqual(result['white_matches'], 5)
        self.assertTrue(result['power_match'])
        self.assertTrue(result['is_jackpot'])
    
    def test_12_random_tickets_are_different(self):
        """Multiple random tickets are likely different"""
        tickets = [self.machine.generate_random_ticket() for _ in range(5)]
        strings = [str(t) for t in tickets]
        # At least some should be different (very unlikely all same)
        self.assertGreater(len(set(strings)), 1)


# ============================================================
# TEST: player.py (15 points)
# ============================================================

class TestPlayer(unittest.TestCase):
    """Test player.py - 15 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'player'
        results[cls.module_name]['total'] = 10
    
    def test_01_import_player(self):
        """player.py can be imported"""
        try:
            from player import Player
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import Player from player.py")
    
    def test_02_player_init(self):
        """Player can be instantiated with initial balance"""
        from player import Player
        player = Player(100)
        self.assertIsNotNone(player)
    
    def test_03_get_balance(self):
        """get_balance returns correct balance"""
        from player import Player
        player = Player(50)
        self.assertEqual(player.get_balance(), 50)
    
    def test_04_get_tickets_empty(self):
        """get_tickets returns empty list initially"""
        from player import Player
        player = Player(100)
        self.assertEqual(player.get_tickets(), [])
    
    def test_05_get_ticket_count(self):
        """get_ticket_count returns correct count"""
        from player import Player
        player = Player(100)
        self.assertEqual(player.get_ticket_count(), 0)
    
    def test_06_can_afford(self):
        """can_afford returns correct boolean"""
        from player import Player
        player = Player(10)
        self.assertTrue(player.can_afford(5))
        self.assertTrue(player.can_afford(10))
        self.assertFalse(player.can_afford(15))
    
    def test_07_deduct_balance(self):
        """deduct_balance reduces balance correctly"""
        from player import Player
        player = Player(100)
        player.deduct_balance(30)
        self.assertEqual(player.get_balance(), 70)
    
    def test_08_add_ticket(self):
        """add_ticket adds ticket to collection"""
        from player import Player
        from lottery_ticket import LotteryTicket
        player = Player(100)
        ticket = LotteryTicket([1, 2, 3, 4, 5], 10)
        player.add_ticket(ticket)
        self.assertEqual(player.get_ticket_count(), 1)
        self.assertIn(ticket, player.get_tickets())
    
    def test_09_buy_ticket(self):
        """buy_ticket deducts $2 and adds ticket"""
        from player import Player
        from lottery_ticket import LotteryTicket
        player = Player(100)
        ticket = LotteryTicket([1, 2, 3, 4, 5], 10)
        player.buy_ticket(ticket)
        self.assertEqual(player.get_balance(), 98)
        self.assertEqual(player.get_ticket_count(), 1)
    
    def test_10_buy_multiple_tickets(self):
        """Player can buy multiple tickets"""
        from player import Player
        from lottery_ticket import LotteryTicket
        player = Player(100)
        for i in range(5):
            ticket = LotteryTicket([1, 2, 3, 4, 5], 10)
            player.buy_ticket(ticket)
        self.assertEqual(player.get_balance(), 90)
        self.assertEqual(player.get_ticket_count(), 5)


# ============================================================
# TEST: display.py (10 points)
# ============================================================

class TestDisplay(unittest.TestCase):
    """Test display.py - 10 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'display'
        results[cls.module_name]['total'] = 8
    
    def setUp(self):
        from display import Display
        self.display = Display()
    
    def test_01_import_display(self):
        """display.py can be imported"""
        try:
            from display import Display
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import Display from display.py")
    
    def test_02_display_init(self):
        """Display can be instantiated"""
        from display import Display
        d = Display()
        self.assertIsNotNone(d)
    
    def test_03_show_welcome_exists(self):
        """show_welcome method exists"""
        self.assertTrue(hasattr(self.display, 'show_welcome'))
    
    def test_04_show_ticket_exists(self):
        """show_ticket method exists"""
        self.assertTrue(hasattr(self.display, 'show_ticket'))
    
    def test_05_show_all_tickets_exists(self):
        """show_all_tickets method exists"""
        self.assertTrue(hasattr(self.display, 'show_all_tickets'))
    
    def test_06_show_winning_numbers_exists(self):
        """show_winning_numbers method exists"""
        self.assertTrue(hasattr(self.display, 'show_winning_numbers'))
    
    def test_07_show_result_exists(self):
        """show_result method exists"""
        self.assertTrue(hasattr(self.display, 'show_result'))
    
    def test_08_show_summary_exists(self):
        """show_summary method exists"""
        self.assertTrue(hasattr(self.display, 'show_summary'))


# ============================================================
# TEST: main.py (10 points)
# ============================================================

class TestMain(unittest.TestCase):
    """Test main.py - 10 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'main'
        results[cls.module_name]['total'] = 5
    
    def test_01_import_main(self):
        """main.py can be imported"""
        try:
            import main
            self.assertTrue(True)
        except ImportError:
            self.fail("Cannot import main.py")
    
    def test_02_main_function_exists(self):
        """main() function exists"""
        import main
        self.assertTrue(hasattr(main, 'main'))
        self.assertTrue(callable(main.main))
    
    def test_03_imports_all_modules(self):
        """main.py imports required modules"""
        import main
        import inspect
        source = inspect.getsource(main)
        
        required_imports = ['Display', 'Player', 'LotteryMachine', 'LotteryTicket']
        for imp in required_imports:
            self.assertIn(imp, source, f"main.py should import {imp}")
    
    def test_04_uses_display_class(self):
        """main.py uses Display class"""
        import main
        import inspect
        source = inspect.getsource(main)
        self.assertIn('Display', source)
    
    def test_05_has_if_name_main(self):
        """main.py has if __name__ == '__main__' block"""
        import main
        import inspect
        source = inspect.getsource(main)
        self.assertIn("if __name__", source)


# ============================================================
# TEST: SRP (5 points)
# ============================================================

class TestSRP(unittest.TestCase):
    """Test Single Responsibility Principle - 5 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'srp'
        results[cls.module_name]['total'] = 5
    
    def test_01_ticket_no_print(self):
        """LotteryTicket does not use print()"""
        import inspect
        from lottery_ticket import LotteryTicket
        source = inspect.getsource(LotteryTicket)
        # Allow print in __str__ but not elsewhere
        lines = source.split('\n')
        in_str_method = False
        for line in lines:
            if 'def __str__' in line:
                in_str_method = True
            elif 'def ' in line and in_str_method:
                in_str_method = False
            if 'print(' in line and not in_str_method:
                self.fail("LotteryTicket should not print directly")
    
    def test_02_ticket_no_random(self):
        """LotteryTicket does not use random"""
        import inspect
        from lottery_ticket import LotteryTicket
        source = inspect.getsource(LotteryTicket)
        self.assertNotIn('random', source, "LotteryTicket should not use random")
    
    def test_03_player_no_print(self):
        """Player does not use print()"""
        import inspect
        from player import Player
        source = inspect.getsource(Player)
        self.assertNotIn('print(', source, "Player should not print directly")
    
    def test_04_player_no_random(self):
        """Player does not use random"""
        import inspect
        from player import Player
        source = inspect.getsource(Player)
        self.assertNotIn('random', source, "Player should not use random")
    
    def test_05_validator_no_print(self):
        """Validator does not use print()"""
        import inspect
        from validator import Validator
        source = inspect.getsource(Validator)
        self.assertNotIn('print(', source, "Validator should not print directly")


# ============================================================
# TEST: Code Style (5 points) - Basic checks
# ============================================================

class TestStyle(unittest.TestCase):
    """Test Code Style - 5 points"""
    
    @classmethod
    def setUpClass(cls):
        cls.module_name = 'style'
        results[cls.module_name]['total'] = 5
    
    def test_01_constants_uses_uppercase(self):
        """constants.py uses UPPERCASE for constants"""
        import constants
        attrs = [a for a in dir(constants) if not a.startswith('_')]
        for attr in attrs:
            self.assertEqual(attr, attr.upper(), f"{attr} should be UPPERCASE")
    
    def test_02_classes_use_camelcase(self):
        """Classes use CamelCase naming"""
        from validator import Validator
        from lottery_ticket import LotteryTicket
        from lottery_machine import LotteryMachine
        from player import Player
        from display import Display
        # If we get here, names are correct
        self.assertTrue(True)
    
    def test_03_files_exist(self):
        """All 7 required files exist"""
        import os
        required = ['constants.py', 'validator.py', 'lottery_ticket.py',
                    'lottery_machine.py', 'player.py', 'display.py', 'main.py']
        for f in required:
            self.assertTrue(os.path.exists(f), f"Missing file: {f}")
    
    def test_04_no_hardcoded_69(self):
        """lottery_machine.py uses constants instead of hardcoded 69"""
        import inspect
        from lottery_machine import LotteryMachine
        source = inspect.getsource(LotteryMachine)
        # Check for WHITE_BALL_MAX usage (should use constant)
        if '69' in source and 'WHITE_BALL_MAX' not in source:
            self.fail("Use WHITE_BALL_MAX constant instead of hardcoded 69")
    
    def test_05_no_hardcoded_26(self):
        """lottery_machine.py uses constants instead of hardcoded 26"""
        import inspect
        from lottery_machine import LotteryMachine
        source = inspect.getsource(LotteryMachine)
        if '26' in source and 'POWER_BALL_MAX' not in source:
            self.fail("Use POWER_BALL_MAX constant instead of hardcoded 26")


# ============================================================
# CUSTOM TEST RESULT CLASS
# ============================================================

class GradingTestResult(unittest.TestResult):
    """Custom test result that tracks results by module"""
    
    def __init__(self):
        super().__init__()
        self.module_results = {}
    
    def addSuccess(self, test):
        super().addSuccess(test)
        module = self._get_module(test)
        if module:
            results[module]['passed'] += 1
    
    def addFailure(self, test, err):
        super().addFailure(test, err)
    
    def addError(self, test, err):
        super().addError(test, err)
    
    def _get_module(self, test):
        test_class = test.__class__
        if hasattr(test_class, 'module_name'):
            return test_class.module_name
        return None


# ============================================================
# GRADING FUNCTION
# ============================================================

def calculate_grades():
    """Calculate final grades based on test results"""
    print("\n" + "=" * 60)
    print("                    GRADING REPORT")
    print("=" * 60 + "\n")
    
    total_points = 0
    max_points = 0
    
    for module, max_pts in POINTS.items():
        data = results[module]
        if data['total'] > 0:
            percentage = data['passed'] / data['total']
            earned = round(percentage * max_pts, 1)
        else:
            earned = 0
        
        data['points'] = earned
        total_points += earned
        max_points += max_pts
        
        # Status bar
        bar_length = 20
        filled = int(bar_length * (earned / max_pts)) if max_pts > 0 else 0
        bar = "#" * filled + "-" * (bar_length - filled)
        
        print(f"{module + '.py':<22} [{bar}] {earned:>5.1f} / {max_pts:<3} pts")
        print(f"                       Tests passed: {data['passed']}/{data['total']}")
        print()
    
    print("=" * 60)
    print(f"{'TOTAL SCORE:':<22} {' ' * 22} {total_points:>5.1f} / {max_points:<3} pts")
    print("=" * 60)
    
    # Grade letter
    percentage = (total_points / max_points) * 100
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"\nFinal Grade: {grade} ({percentage:.1f}%)")
    print()
    
    return total_points, max_points


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    # Add current directory to path
    import os
    sys.path.insert(0, os.getcwd())
    
    print("\n" + "=" * 60)
    print("         LOTTERY SYSTEM - AUTOMATED GRADING")
    print("=" * 60)
    print("\nRunning tests...\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestConstants))
    suite.addTests(loader.loadTestsFromTestCase(TestValidator))
    suite.addTests(loader.loadTestsFromTestCase(TestLotteryTicket))
    suite.addTests(loader.loadTestsFromTestCase(TestLotteryMachine))
    suite.addTests(loader.loadTestsFromTestCase(TestPlayer))
    suite.addTests(loader.loadTestsFromTestCase(TestDisplay))
    suite.addTests(loader.loadTestsFromTestCase(TestMain))
    suite.addTests(loader.loadTestsFromTestCase(TestSRP))
    suite.addTests(loader.loadTestsFromTestCase(TestStyle))
    
    # Run with custom result
    result = GradingTestResult()
    
    # Suppress test output
    with redirect_stdout(io.StringIO()):
        suite.run(result)
    
    # Show failures and errors
    if result.failures or result.errors:
        print("-" * 60)
        print("FAILED TESTS:")
        print("-" * 60)
        for test, trace in result.failures:
            print(f"\n[FAIL] {test}")
            # Print only the assertion message, not full trace
            lines = trace.strip().split('\n')
            print(f"   {lines[-1]}")
        
        for test, trace in result.errors:
            print(f"\n[ERROR] {test}")
            lines = trace.strip().split('\n')
            print(f"   {lines[-1]}")
        print()
    
    # Calculate and display grades
    calculate_grades()
