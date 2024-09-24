$(document).ready(function () {
  // Handle Unified Login
  $("#loginForm").submit(function (event) {
    event.preventDefault();

    const loginData = {
      email: $("#email").val(),
      password: $("#password").val(),
      role: $("#roleSelect").val(), // Get the selected role (patient/doctor)
    };

    $.ajax({
      url: "/api/login",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(loginData),
      success: (resp) => {
        alert(resp.message);
        if (loginData.role === "patient") {
          window.location.href = "/patient-dashboard";
        } else {
          window.location.href = "/doctor-dashboard";
        }
      },
      error: function (xhr) {
        alert("Error logging in: " + xhr.responseText);
      },
    });
  });
});
