<?php
# Debug mode
$debug = true;

if ($debug) {
	echo "<pre>\n";
}

$shellCommand['pyVersion'] = "python3";
$shellCommand['scriptName'] = realpath(dirname(__FILE__) . "/script_python/client.py");

if ($debug) {
	$shellCommand['verbose'] = "--verbose";
}

if (!empty($_POST)) {
	$shellCommand['order'] = $_POST['order'];
}

$shellCommand['STDOUT'] = "2>&1";

if (!empty($shellCommand['scriptName'])) {
	$command = implode(" ", $shellCommand);
	$output = explode("\n", shell_exec($command));
	if ($debug) {
		echo "[SCRIPT] command: $command \n";
		foreach ($output as $key => $value) {
			if (!empty($value)) {
				echo "[OUTPUT] $value\n";
			}
		}
	}
} else {
	echo "[SCRIPT] ERROR: Can't find the script !\n";
}

if ($debug) {
	echo "<pre>\n";
}

?>
