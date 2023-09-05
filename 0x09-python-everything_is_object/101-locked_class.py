#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """this precents a user from enteribg an instance that isn't first_name"""
    __slots__ = ["first_name"]
