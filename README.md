<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>BMI Calculator</h1>

<p>This is a simple Python-based BMI (Body Mass Index) calculator that allows users to input their height and weight, calculates their BMI, and provides a health category based on the BMI value.</p>

<h2>Description</h2>
<p>The BMI Calculator is a command-line program that helps users understand their body weight category based on their height and weight. By entering these two values, the program calculates the BMI using a standard formula and classifies the result into one of four categories: Underweight, Normal weight, Overweight, or Obesity. This tool is useful for quick health assessments, fitness tracking, and personal wellness monitoring.</p>

<h2>Features</h2>
<ul>
    <li><strong>Simple User Input:</strong> Users can easily input their height and weight.</li>
    <li><strong>BMI Calculation:</strong> Automatically calculates BMI using the formula: <code>BMI = weight (kg) / height (m)^2</code>.</li>
    <li><strong>Health Category Classification:</strong> Provides a health classification based on BMI:
        <ul>
            <li>Underweight: BMI &lt; 18.5</li>
            <li>Normal weight: 18.5 ≤ BMI &lt; 24.9</li>
            <li>Overweight: 25 ≤ BMI &lt; 29.9</li>
            <li>Obesity: BMI ≥ 30</li>
        </ul>
    </li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Clone or download this repository.</li>
    <li>Open a terminal or command prompt in the directory containing the file.</li>
    <li>Run the following command to start the program:</li>
    <pre><code>python bmi_calculator.py</code></pre>
    <li>Enter your height (in meters) and weight (in kilograms) when prompted.</li>
    <li>The program will display your calculated BMI and health category.</li>
</ol>

<h2>Example</h2>
<pre><code>Enter your height in meters: 1.75
Enter your weight in kilograms: 70
Your BMI is 22.86, which falls under the category: Normal weight</code></pre>

<h2>Code Overview</h2>
<p>The program uses three main steps:</p>
<ol>
    <li><strong>Collects User Input:</strong> It prompts the user to enter their height and weight using the <code>input()</code> function.</li>
    <li><strong>Calculates BMI:</strong> Computes BMI using the formula <code>weight / (height ** 2)</code>.</li>
    <li><strong>Classifies BMI:</strong> Uses conditional statements to categorize BMI into Underweight, Normal weight, Overweight, or Obesity.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

</body>
</html>
