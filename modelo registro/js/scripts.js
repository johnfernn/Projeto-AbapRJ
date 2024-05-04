document.getElementById('exampleInputFile').addEventListener('change', function(event) {
    var input = event.target;
    var reader = new FileReader();

    reader.onload = function(){
        var dataURL = reader.result;
        var imgElement = document.createElement('img');
        imgElement.src = dataURL;
        document.getElementById('imagePreview').innerHTML = ''; // Limpa qualquer imagem anterior
        document.getElementById('imagePreview').appendChild(imgElement);
    };

    reader.readAsDataURL(input.files[0]);
});