// Add a click event handler to the <div> element with id toggle_header
$('#toggle_header').click(function() {
    // Select the <header> element
    var header = $('header');
    
    // Check if the header has class 'red'
    if (header.hasClass('red')) {
        // If it has class 'red', toggle to 'green'
        header.removeClass('red').addClass('green');
    } else {
        // If it doesn't have class 'red', toggle to 'red'
        header.removeClass('green').addClass('red');
    }
});
