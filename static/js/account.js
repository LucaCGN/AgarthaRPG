// For the Registration Page
$("#registerForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: "/register",
    type: "POST",
    data: JSON.stringify({
      user_name: $("#username").val(),
      user_surname: $("#surname").val(),
      user_birthday: $("#birthday").val(),
      user_email: $("#email").val(),
      user_password: $("#password").val()
    }),
    contentType: "application/json",
    success: function(response) {
      alert(response.message);
      if (response.message === "User registered successfully") {
        window.location.href = "/email_verification";
      }
    },
    error: function(error) {
      alert(error.responseJSON.message);
    }
  });
});


// For the Email Verification Page
$("#emailVerificationForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: "/verify_email",  // Replace with your Flask route for email verification
    type: "POST",
    data: JSON.stringify({
      email: $("#email").val(),
      verification_code: $("#verificationCode").val()
    }),
    contentType: "application/json",
    success: function(response) {
      alert(response.message);
      if (response.message === "Email verified") {
        window.location.href = "/begin_creation";  // Redirect to begin creation page
      }
    },
    error: function(error) {
      alert(error.responseJSON.message);
    }
  });
});


// For the Login Page
$("#loginForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: "/login",  // Replace with your Flask route for login
    type: "POST",
    data: JSON.stringify({
      email: $("#email").val(),
      password: $("#password").val()
    }),
    contentType: "application/json",
    success: function(response) {
      alert("Logged in successfully");
      // Store the token and redirect to the dashboard or main page
      localStorage.setItem("token", response.token);
      window.location.href = "/dashboard";  // Replace with your main page route
    },
    error: function(error) {
      alert(error.responseJSON.message);
    }
  });
});

// For the Password Reset Page
$("#passwordResetForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: "/send_reset_password_email",  // Replace with your Flask route for sending reset password email
    type: "POST",
    data: JSON.stringify({
      email: $("#email").val()
    }),
    contentType: "application/json",
    success: function(response) {
      alert(response.message);
    },
    error: function(error) {
      alert(error.responseJSON.message);
    }
  });
});

// For requesting a new verification email
$("#requestVerificationEmailForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: "/api/email-verification",
    type: "POST",
    data: JSON.stringify({ email: $("#email").val() }),
    contentType: "application/json",
    success: function(response) {
      alert(response.message);
    },
    error: function(error) {
      alert(error.responseJSON.message);
    }
  });
});

// For actually resetting the password
$("#actualPasswordResetForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: "/api/reset-password",
    type: "POST",
    data: JSON.stringify({
      email: $("#email").val(),
      new_password: $("#newPassword").val(),
      reset_token: $("#resetToken").val()
    }),
    contentType: "application/json",
    success: function(response) {
      alert(response.message);
      if (response.message === "Password reset successfully") {
        window.location.href = "/login";
      }
    },
    error: function(error) {
      alert(error.responseJSON.message);
    }
  });
});
