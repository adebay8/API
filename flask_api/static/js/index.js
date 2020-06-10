var submitbtn = document.getElementById("#button");
var input = document.getElementById("#input");
submitbtn.addEventListener("click", display());
        
function display(event){
    event.preventDefault();
    var inputvalue = input.value;
    window.location.replace(" http://127.0.0.1:5000/api/v1/resources/books/?"+ inputvalue);

}