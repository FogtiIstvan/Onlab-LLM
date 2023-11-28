<?php
// Define the path to the Python interpreter and the Python script
$pythonPath = '/usr/bin/python3';
$scriptPath = '/var/www/html/Testphp/LLM.py';

// Define the arguments
$arg1 = 'arg1';
$arg2 = 'arg2';

// Execute the Python script with the arguments
$output = shell_exec("$pythonPath $scriptPath $arg1 $arg2");

// Output the return value
echo $output;
?>