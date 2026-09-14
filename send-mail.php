<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $first_name = isset($_POST['first_name']) ? trim(filter_var($_POST['first_name'], FILTER_SANITIZE_FULL_SPECIAL_CHARS)) : '';
    $last_name  = isset($_POST['last_name'])  ? trim(filter_var($_POST['last_name'], FILTER_SANITIZE_FULL_SPECIAL_CHARS))  : '';
    $phone      = isset($_POST['phone'])      ? trim(filter_var($_POST['phone'], FILTER_SANITIZE_FULL_SPECIAL_CHARS))      : '';
    $email      = isset($_POST['email'])      ? trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL))     : '';
    $subject    = isset($_POST['subject'])    ? trim(filter_var($_POST['subject'], FILTER_SANITIZE_FULL_SPECIAL_CHARS))    : '';
    $message    = isset($_POST['message'])    ? trim(filter_var($_POST['message'], FILTER_SANITIZE_FULL_SPECIAL_CHARS))    : '';

    if (empty($first_name) || empty($phone) || empty($message)) {
        echo json_encode(["status" => "error", "message" => "Please fill in all required fields (Name, Phone, and Message)."]);
        exit;
    }

    $to = "intact999@gmail.com";
    $email_subject = "New Website Inquiry: " . ($subject ? $subject : "General Product Inquiry");
    
    $body = "You have received a new message from the INTACT website contact form:\n\n";
    $body .= "Name: " . $first_name . " " . $last_name . "\n";
    $body .= "Phone: " . $phone . "\n";
    $body .= "Email: " . ($email ? $email : "N/A") . "\n";
    $body .= "Subject: " . $subject . "\n";
    $body .= "Message:\n" . $message . "\n";

    $headers = "From: webmaster@intactpanel.com\r\n";
    if (!empty($email)) {
        $headers .= "Reply-To: " . $email . "\r\n";
    }

    // Attempt to send email
    @mail($to, $email_subject, $body, $headers);

    echo json_encode(["status" => "success", "message" => "Thank you! Your inquiry has been received. Our team will contact you shortly."]);
    exit;
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request method."]);
    exit;
}
