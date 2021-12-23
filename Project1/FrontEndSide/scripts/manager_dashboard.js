console.log("hit!")
// logout button
let logoutBtn = document.getElementById("logout-btn");
logoutBtn.onclick = function(){
    window.location.href = "index.html";
}


let allBtn = document.getElementById("all-reimb");
allBtn.onclick = function(){
    window.location.href = "manager_dashboard.html";
}

//approve bottun
let resolveReimForm = document.getElementById("resolve-reimb-form");
let approveReimb = document.getElementById("approve-reimb");
let denyReimb = document.getElementById("deny-reimb");

approveReimb.onclick = async function(e){
    e.preventDefault();

    let reimbResolveInput = document.getElementById("reimb-resolve-input").value;

    let reimbResolvecomment = document.getElementById("reimb-resolve-comment").value;

    if(reimbResolveInput != null){
        let approveReimbRes = await fetch(`http://127.0.0.1:5000/reimbursement`, {
            method: "PATCH",
            body: JSON.stringify({
            reimbursementId : reimbResolveInput,
            reimbursementTypeId : null,
            reimbursementAmount : null,
            dateSubmitted : null,
            dateResolved : null,
            reimbursementtatusId : "Approved",
            reimbursementEmployeeId : null,
            managerComment : reimbResolvecomment          
            })
        })

        let approveReimbResData = await approveReimbRes.json();

        if(approveReimbResData.reimbursementId>0){
            alert("successfully Approved!")
        }

    }    
}

denyReimb.onclick = async function(e){
    e.preventDefault();

    let reimbDenyInput = document.getElementById("reimb-resolve-input").value;

    let reimbResolvecomment = document.getElementById("reimb-resolve-comment").value;

    if(reimbDenyInput != null){
        let DenyReimbRes = await fetch(`http://127.0.0.1:5000/reimbursement`, {
            method: "PATCH",
            body: JSON.stringify({
            reimbursementId : reimbDenyInput,
            reimbursementTypeId : null,
            reimbursementAmount : null,
            dateSubmitted : null,
            dateResolved : null,
            reimbursementtatusId : "Denied",
            reimbursementEmployeeId : null,
            managerComment : reimbResolvecomment          
            })
        })

        let denyReimbResData = await DenyReimbRes.json();

        if(denyReimbResData.reimbursementId>0){
            alert("successfully Denied!")
        }

    }    
}














window.onload = async function(){
    getAllRiembursements();
}


async function getAllRiembursements(){
    let url = `http://127.0.0.1:5000/allreim`
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


let pendingBtn = document.getElementById("pending-reimb");
pendingBtn.onclick = async function(e){
    e.preventDefault();   

    let url = `http://127.0.0.1:5000/reimbursement/pending`
    let response = await fetch(url);
    let body = await response.json();
    console.log(body)


    let reimbTableElem = document.getElementById("reimb-table");
    reimbTableElem.innerHTML = ``;


    reimbTableElem.innerHTML += `       
            <tr>
                 <th>Request ID</th>
                 <th>Type</th>
                  <th>Amount</th>
                  <th>Date Submitted</th>
                  <th>Date Resolved</th>
                  <th>Status</th>
                  <th>Employee ID</th>
                  <th>Manager Comment</th>
            </tr>  
    `;          



    //iterate through each employee's reimbursement request
      body.forEach(reimbRequest => {

        let tableRow2 = document.createElement("tr");

        let dataIdElem = document.createElement("td");
        dataIdElem.innerText = reimbRequest.reimbursementId;
        tableRow2.appendChild(dataIdElem);

        let dataTypeElem = document.createElement("td");
        dataTypeElem.innerText = reimbRequest.reimbursementTypeId;
        tableRow2.appendChild(dataTypeElem);

        let dataAmountElem = document.createElement("td");
        dataAmountElem.innerText = reimbRequest.reimbursementAmount;
        tableRow2.appendChild(dataAmountElem);

        let dataSubmittedElem = document.createElement("td");
        dataSubmittedElem.innerText = reimbRequest.dateSubmitted;
        tableRow2.appendChild(dataSubmittedElem);

        let dataResolvedElem = document.createElement("td");
        dataResolvedElem.innerText = reimbRequest.dateResolved;
        tableRow2.appendChild(dataResolvedElem);

        let dataStatusElem = document.createElement("td");
        dataStatusElem.innerText = reimbRequest.reimbursementtatusId;
        tableRow2.appendChild(dataStatusElem);
        

        let dataEployeeIDElem = document.createElement("td");
        dataEployeeIDElem.innerText = reimbRequest.reimbursementEmployeeId;
        tableRow2.appendChild(dataEployeeIDElem);

        let dataCommentElem = document.createElement("td");
        dataCommentElem.innerText = reimbRequest.managerComment;
        tableRow2.appendChild(dataCommentElem);

        reimbTableElem.appendChild(tableRow2);
       
       

    });
   


  

   
}


let approvedBtn = document.getElementById("approved-reimb");
approvedBtn.onclick = async function(e){
    e.preventDefault();   

    let url = `http://127.0.0.1:5000/reimbursement/approved`
    let response = await fetch(url);
    let body = await response.json();
    console.log(body)


    let reimbTableElem = document.getElementById("reimb-table");
    reimbTableElem.innerHTML = ``;


    reimbTableElem.innerHTML += `       
            <tr>
                 <th>Request ID</th>
                 <th>Type</th>
                  <th>Amount</th>
                  <th>Date Submitted</th>
                  <th>Date Resolved</th>
                  <th>Status</th>
                  <th>Employee ID</th>
                  <th>Manager Comment</th>
            </tr>  
    `;          



    //iterate through each employee's reimbursement request
      body.forEach(reimbRequest => {

        let tableRow2 = document.createElement("tr");

        let dataIdElem = document.createElement("td");
        dataIdElem.innerText = reimbRequest.reimbursementId;
        tableRow2.appendChild(dataIdElem);

        let dataTypeElem = document.createElement("td");
        dataTypeElem.innerText = reimbRequest.reimbursementTypeId;
        tableRow2.appendChild(dataTypeElem);

        let dataAmountElem = document.createElement("td");
        dataAmountElem.innerText = reimbRequest.reimbursementAmount;
        tableRow2.appendChild(dataAmountElem);

        let dataSubmittedElem = document.createElement("td");
        dataSubmittedElem.innerText = reimbRequest.dateSubmitted;
        tableRow2.appendChild(dataSubmittedElem);

        let dataResolvedElem = document.createElement("td");
        dataResolvedElem.innerText = reimbRequest.dateResolved;
        tableRow2.appendChild(dataResolvedElem);

        let dataStatusElem = document.createElement("td");
        dataStatusElem.innerText = reimbRequest.reimbursementtatusId;
        tableRow2.appendChild(dataStatusElem);
        

        let dataEployeeIDElem = document.createElement("td");
        dataEployeeIDElem.innerText = reimbRequest.reimbursementEmployeeId;
        tableRow2.appendChild(dataEployeeIDElem);

        let dataCommentElem = document.createElement("td");
        dataCommentElem.innerText = reimbRequest.managerComment;
        tableRow2.appendChild(dataCommentElem);

        reimbTableElem.appendChild(tableRow2);
       
       

    });
   


  

   
}