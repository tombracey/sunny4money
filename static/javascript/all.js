$(function () {
    $('form'.validate();

    $('form'.on('submit', function(e) {
        e.preventDefault();

        let dataString = $(this).seralize();

        $.ajax({
            type: 'POST',
            url: 'bin/process.php',
            data: dataString
        })
    }
))
}
)