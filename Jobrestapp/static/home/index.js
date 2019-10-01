function searchForApplicant(){
  let searchInputValue = GetInputValue('search-input')
  let searchBasedOn = GetInputValue('search-based-on')
  location.href = '/search?searchBasedOn=' + searchBasedOn
    + '&searchInputValue=' + searchInputValue
}


function GetInputValue(inputId){
  var inputValue = document.getElementById(inputId).value;
  return inputValue;
}
