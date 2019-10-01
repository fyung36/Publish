function Submit(){

  let applicantData = {
    FirstName: GetInputValue('firstname'),
    LastName: GetInputValue('lastname'),
    Email: GetInputValue('email'),
    Age: GetInputValue('age'),
    Job_Position: GetInputValue('job_position'),
  }
  axios.post('/add-applicant/', {applicantData: applicantData}).then((response) => {
    location.href = '/'
  })
  .catch((error) => {

  })

}

function GetInputValue(inputId){
  var inputValue = document.getElementById(inputId).value;
  return inputValue;
}
