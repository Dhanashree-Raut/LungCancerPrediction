<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "contact";

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) 
    {
        die("Connection failergsrgsegd: " . $conn->connect_error);
    }

        $fname=$_REQUEST['name'];
        $lname=$_REQUEST['surname'];
        $email=$_REQUEST['email'];
        $topic=$_REQUEST['topic'];
        $message=$_REQUEST['message'];


     $sql = "INSERT INTO contact_us values('$fname','$lname','$topic','$message','$email')";

  // $sql = "INSERT INTO contact_us values('aa','asn'a','agjah','pok@fhrf')";

        if (mysqli_query($conn,$sql)) 
        {
            echo "New record created successfully";
        } 
        else 
        {
            echo "Error:";
        }

    $conn->close();
    ?>