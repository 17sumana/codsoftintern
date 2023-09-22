{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "04e76cd8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select operation.\n",
      "1.Add\n",
      "2.Subtract\n",
      "3.Multiply\n",
      "4.Divide\n",
      "Enter choice(1/2/3/4): 1\n",
      "Enter first number: 23\n",
      "Enter second number: 34\n",
      "23.0 + 34.0 = 57.0\n",
      "Let's do next calculation? (yes/no): yes\n",
      "Enter choice(1/2/3/4): 3\n",
      "Enter first number: 4\n",
      "Enter second number: 5\n",
      "4.0 * 5.0 = 20.0\n",
      "Let's do next calculation? (yes/no): yes\n",
      "Enter choice(1/2/3/4): 2\n",
      "Enter first number: 3\n",
      "Enter second number: 2\n",
      "3.0 - 2.0 = 1.0\n",
      "Let's do next calculation? (yes/no): 4\n",
      "Enter choice(1/2/3/4): 35\n",
      "Invalid Input\n",
      "Enter choice(1/2/3/4): 5\n",
      "Invalid Input\n",
      "Enter choice(1/2/3/4): no\n",
      "Invalid Input\n",
      "Enter choice(1/2/3/4): 3\n",
      "Enter first number: 6\n",
      "Enter second number: 5\n",
      "6.0 * 5.0 = 30.0\n",
      "Let's do next calculation? (yes/no): no\n"
     ]
    }
   ],
   "source": [
    "# This function adds two numbers\n",
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "# This function subtracts two numbers\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "# This function multiplies two numbers\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "# This function divides two numbers\n",
    "def divide(x, y):\n",
    "    return x / y\n",
    "\n",
    "\n",
    "print(\"Select operation.\")\n",
    "print(\"1.Add\")\n",
    "print(\"2.Subtract\")\n",
    "print(\"3.Multiply\")\n",
    "print(\"4.Divide\")\n",
    "\n",
    "while True:\n",
    "    # take input from the user\n",
    "    choice = input(\"Enter choice(1/2/3/4): \")\n",
    "\n",
    "    # check if choice is one of the four options\n",
    "    if choice in ('1', '2', '3', '4'):\n",
    "        try:\n",
    "            num1 = float(input(\"Enter first number: \"))\n",
    "            num2 = float(input(\"Enter second number: \"))\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a number.\")\n",
    "            continue\n",
    "\n",
    "        if choice == '1':\n",
    "            print(num1, \"+\", num2, \"=\", add(num1, num2))\n",
    "\n",
    "        elif choice == '2':\n",
    "            print(num1, \"-\", num2, \"=\", subtract(num1, num2))\n",
    "\n",
    "        elif choice == '3':\n",
    "            print(num1, \"*\", num2, \"=\", multiply(num1, num2))\n",
    "\n",
    "        elif choice == '4':\n",
    "            print(num1, \"/\", num2, \"=\", divide(num1, num2))\n",
    "        \n",
    "        # check if user wants another calculation\n",
    "        # break the while loop if answer is no\n",
    "        next_calculation = input(\"Let's do next calculation? (yes/no): \")\n",
    "        if next_calculation == \"no\":\n",
    "          break\n",
    "    else:\n",
    "        print(\"Invalid Input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f59bca5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
