#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutExceptions(Koan):
    class MySpecialError(RuntimeError):
        pass

    def test_exceptions_inherit_from_exception(self):
        mro = self.MySpecialError.mro()
        print("\n", mro, "\n")
        self.assertEqual("RuntimeError", mro[1].__name__)
        self.assertEqual("Exception", mro[2].__name__)
        self.assertEqual("BaseException", mro[3].__name__)
        self.assertEqual("object", mro[4].__name__)

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = "exception handled"

            ex2 = ex

        self.assertEqual("exception handled", result)

        self.assertEqual(True, isinstance(ex2, Exception))
        self.assertEqual(False, isinstance(ex2, RuntimeError))

        self.assertTrue(
            issubclass(RuntimeError, Exception),
            "RuntimeError is a subclass of Exception",
        )
        self.assertEqual("Oops", ex2.args[0])

    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = "exception handled"
            msg = ex.args[0]

        self.assertEqual("exception handled", result)
        self.assertEqual("My Message", msg)

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = "it broke"
            pass
        else:
            result = "no damage done"

        self.assertEqual("no damage done", result)

    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = "always run"

        self.assertEqual("always run", result)
