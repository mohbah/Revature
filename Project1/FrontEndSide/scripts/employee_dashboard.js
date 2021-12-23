console.log("employee-dashboard.js hit!");

const EmployeeID = sessionStorage.getItem("value");

let logoutBtn = document.getElementById("logout-btn");
logoutBtn.onclick = function(){
    window.location.href = "index.html";
}
 





window.onload = async function(){
    getAllRiembursements();
}


async function getAllRiembursements(){
    let url = `http://127.0.0.1:5000/employee/${EmployeeID}`
    let response = await fetch(url);
    let body = await response.json();
    console.log(body)


    let reimbTableElem = document.getElementById("reimb-table");


    //iterate through each employee's reimbursement request
      body.forEach(reimbRequest => {

        let tableRow = document.createElement("tr");

        let dataIdElem = document.createElement("td");
        dataIdElem.innerText = reimbRequest.reimbursementId;
        tableRow.appendChild(dataIdElem);

        let dataTypeElem = document.createElement("td");
        dataTypeElem.innerText = reimbRequest.reimbursementTypeId;
        tableRow.appendChild(dataTypeElem);

        let dataAmountElem = document.createElement("td");
        dataAmountElem.innerText = reimbRequest.reimbursementAmount;
        tableRow.appendChild(dataAmountElem);

        let dataSubmittedElem = document.createElement("td");
        dataSubmittedElem.innerText = reimbRequest.dateSubmitted;
        tableRow.appendChild(dataSubmittedElem);

        let dataResolvedElem = document.createElement("td");
        dataResolvedElem.innerText = reimbRequest.dateResolved;
        tableRow.appendChild(dataResolvedElem);

        let dataStatusElem = document.createElement("td");
        dataStatusElem.innerText = reimbRequest.reimbursementtatusId;
        tableRow.appendChild(dataStatusElem);
        

        let dataEployeeIDElem = document.createElement("td");
        dataEployeeIDElem.innerText = reimbRequest.reimbursementEmployeeId;
        tableRow.appendChild(dataEployeeIDElem);

        let dataCommentElem = document.createElement("td");
        dataCommentElem.innerText = reimbRequest.managerComment;
        tableRow.appendChild(dataCommentElem);

        reimbTableElem.appendChild(tableRow);
       
       

    });



}

let newReimbBtn = document.getElementById("new-reimb-btn");
newReimbBtn.onclick = function(){
    window.location.href = "new-reimbursement.html";
};




