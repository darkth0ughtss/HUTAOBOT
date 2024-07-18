# BOT/features/math.py

from .. import app as bot
from pyrogram import filters
import math

@bot.on_message(filters.command("add"))
def add(client, message):
    try:
        numbers = message.text.split()[1:]
        if len(numbers) != 2:
            message.reply_text("⚠️ Please provide exactly two numbers.")
            return
        num1, num2 = map(float, numbers)
        result = num1 + num2
        message.reply_text(f"➕ The result of {num1} + {num2} is {result}")
    except ValueError:
        message.reply_text("❌ Please provide valid numbers.")

@bot.on_message(filters.command("subtract"))
def subtract(client, message):
    try:
        numbers = message.text.split()[1:]
        if len(numbers) != 2:
            message.reply_text("⚠️ Please provide exactly two numbers.")
            return
        num1, num2 = map(float, numbers)
        result = num1 - num2
        message.reply_text(f"➖ The result of {num1} - {num2} is {result}")
    except ValueError:
        message.reply_text("❌ Please provide valid numbers.")

@bot.on_message(filters.command("multiply"))
def multiply(client, message):
    try:
        numbers = message.text.split()[1:]
        if len(numbers) != 2:
            message.reply_text("⚠️ Please provide exactly two numbers.")
            return
        num1, num2 = map(float, numbers)
        result = num1 * num2
        message.reply_text(f"✖️ The result of {num1} * {num2} is {result}")
    except ValueError:
        message.reply_text("❌ Please provide valid numbers.")

@bot.on_message(filters.command("divide"))
def divide(client, message):
    try:
        numbers = message.text.split()[1:]
        if len(numbers) != 2:
            message.reply_text("⚠️ Please provide exactly two numbers.")
            return
        num1, num2 = map(float, numbers)
        if num2 == 0:
            message.reply_text("🚫 Cannot divide by zero.")
            return
        result = num1 / num2
        message.reply_text(f"➗ The result of {num1} / {num2} is {result}")
    except ValueError:
        message.reply_text("❌ Please provide valid numbers.")

@bot.on_message(filters.command("factorial"))
def factorial(client, message):
    try:
        number = int(message.text.split()[1])
        result = math.factorial(number)
        message.reply_text(f"🔢 The factorial of {number} is {result}")
    except (ValueError, IndexError):
        message.reply_text("❌ Please provide a valid non-negative integer.")

@bot.on_message(filters.command("power"))
def power(client, message):
    try:
        numbers = message.text.split()[1:]
        if len(numbers) != 2:
            message.reply_text("⚠️ Please provide exactly two numbers.")
            return
        base, exp = map(float, numbers)
        result = math.pow(base, exp)
        message.reply_text(f"⚡ The result of {base} raised to the power of {exp} is {result}")
    except ValueError:
        message.reply_text("❌ Please provide valid numbers.")

@bot.on_message(filters.command("gcd"))
def gcd(client, message):
    try:
        numbers = message.text.split()[1:]
        if len(numbers) != 2:
            message.reply_text("⚠️ Please provide exactly two numbers.")
            return
        num1, num2 = map(int, numbers)
        result = math.gcd(num1, num2)
        message.reply_text(f"🔍 The greatest common divisor of {num1} and {num2} is {result}")
    except ValueError:
        message.reply_text("❌ Please provide valid integers.")

@bot.on_message(filters.command("sqrt"))
def sqrt(client, message):
    try:
        number = float(message.text.split()[1])
        result = math.sqrt(number)
        message.reply_text(f"√ The square root of {number} is {result}")
    except (ValueError, IndexError):
        message.reply_text("❌ Please provide a valid number.")
