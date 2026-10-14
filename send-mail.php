<?php
header('Content-Type: application/json; charset=utf-8');

$method = strtoupper($_SERVER['REQUEST_METHOD'] ?? '');
if ($method !== 'POST' && empty($_POST)) {
    echo json_encode([
        "status" => "error", 
        "message" => "Invalid request method. Only POST submissions are allowed."
    ]);
    exit;
}

// Sanitize & collect inputs (prefer $_POST, fallback to $_REQUEST)
$inputData = !empty($_POST) ? $_POST : $_REQUEST;
$name    = isset($inputData['name']) ? trim(strip_tags($inputData['name'])) : '';
$phone   = isset($inputData['phone']) ? trim(strip_tags($inputData['phone'])) : '';
$email   = isset($inputData['email']) ? trim(filter_var($inputData['email'], FILTER_SANITIZE_EMAIL)) : '';
$product = isset($inputData['product']) ? trim(strip_tags($inputData['product'])) : '';
$message = isset($inputData['message']) ? trim(strip_tags($inputData['message'])) : '';

// 1. Validate Name
if (empty($name) || mb_strlen($name) < 2) {
    echo json_encode([
        "status" => "error", 
        "message" => "Please enter your full name (at least 2 characters)."
    ]);
    exit;
}

// 2. Validate Phone (Clean and check for 10 digits)
$cleanPhone = preg_replace('/[^0-9]/', '', $phone);
if (strlen($cleanPhone) === 12 && substr($cleanPhone, 0, 2) === '91') {
    $cleanPhone = substr($cleanPhone, 2);
}

if (empty($cleanPhone) || !preg_match('/^[0-9]{10}$/', $cleanPhone)) {
    echo json_encode([
        "status" => "error", 
        "message" => "Please enter a valid 10-digit mobile number."
    ]);
    exit;
}

// 3. Validate Email
if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode([
        "status" => "error", 
        "message" => "Please enter a valid email address."
    ]);
    exit;
}

// 4. Validate Product Category
if (empty($product)) {
    echo json_encode([
        "status" => "error", 
        "message" => "Please select a product category."
    ]);
    exit;
}

// 5. Validate Message
if (empty($message) || mb_strlen($message) < 5) {
    echo json_encode([
        "status" => "error", 
        "message" => "Please describe your project requirements (at least 5 characters)."
    ]);
    exit;
}

// Configuration
$to = "intactdesign11@gmail.com, info@intactdesignextrusion.com";
$email_subject = "INTACT Website Enquiry: " . $product . " - " . $name;

$body  = "New Product Enquiry received from intactdesignextrusion.com:\n\n";
$body .= "--------------------------------------------------\n";
$body .= "Name:            " . $name . "\n";
$body .= "Phone:           +91 " . $cleanPhone . "\n";
$body .= "Email:           " . $email . "\n";
$body .= "Product/Category:" . $product . "\n";
$body .= "--------------------------------------------------\n";
$body .= "Message / Requirements:\n" . $message . "\n";
$body .= "--------------------------------------------------\n";
$body .= "Submitted At:    " . date("d-M-Y H:i:s") . " (IST)\n";
$body .= "IP Address:      " . ($_SERVER['REMOTE_ADDR'] ?? 'Unknown') . "\n";

$headers  = "From: INTACT Website <info@intactdesignextrusion.com>\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// Attempt to send email
@mail($to, $email_subject, $body, $headers);

echo json_encode([
    "status" => "success", 
    "message" => "Thank you, " . htmlspecialchars($name, ENT_QUOTES, 'UTF-8') . "! Your product enquiry has been received successfully. Our sales team will get back to you shortly."
]);
exit;
