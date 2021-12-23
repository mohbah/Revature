let logoutBtn = document.getElementById("logout-btn");
logoutBtn.onclick = function(){
    window.location.href = "index.html";
}

let backBtn = document.getElementById("back-btn");
backBtn.onclick = function(){
    window.location.href = "employee_dashboard.html";
}

const EmployeeID = sessionStorage.getItem("value");

console.log(EmployeeID)

let newReimbForm = document.getElementById("new-reimb-form")

newReimbForm.onsubmit = async function(e){
    e.preventDefault();

    let reimbAmount = document.getElementById("amount").value;
    console.log(reimbAmount);

   

    let reimbType = document.getElementById("type-selector").value;
    console.log(reimbType);

    let response = await fetch(`http://127.0.0.1:5000/reimbursement`, {
        method : "POST",
        body : JSON.stringify({
            reimbursementId : null,
            reimbursementTypeId : reimbType,
            reimbursementAmount : reimbAmount,
            dateSubmitted : null,
            dateResolved : null,
            reimbursementtatusId : null,
            reimbursementEmployeeId : EmployeeID,
            managerComment : null           
        })
    });

    let responseData = await response.json();
    console.log(responseData);

    if(responseData.reimbursementId > 0){
        alert('Successfully Submitted!')
    }


}
