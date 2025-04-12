$(document).ready(function() {
    $('#sunnyForm').on('submit', function(e) {
        e.preventDefault();  // Prevent the form from submitting normally

        // Show loading spinner
        $('#loading').show();

        // Collect form data
        var formData = $(this).serialize();

        // Send AJAX request
        $.ajax({
            url: "{% url 'your_view_name' %}",  // Replace with your view URL
            type: "POST",
            data: formData,
            success: function(response) {
                // Hide loading spinner
                $('#loading').hide();

                // Update the results section with the response from the server
                $('#results').html(response);
            },
            error: function() {
                // Hide loading spinner
                $('#loading').hide();
                alert("There was an error processing your request. Please try again.");
            }
        });
    });
});