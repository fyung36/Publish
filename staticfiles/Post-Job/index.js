function Submit(){

  let JobData = {
    Job_title: GetInputValue('Jobtitle'),
    Job_Description: GetInputValue('Job_description'),
    Company: GetInputValue('Company'),

  }
  axios.post('/add-jobs/', {JobData: JobData}).then((response) => {
    location.href = '/'
  })
  .catch((error) => {

  })

}

function GetInputValue(inputId){
  var inputValue = document.getElementById(inputId).value;
  return inputValue;
}
