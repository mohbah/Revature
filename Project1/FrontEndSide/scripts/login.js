let loginForm = document.getElementById("login-form")




loginForm.onsubmit = async function(e){
    e.preventDefault();
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    console.log(username, password)
    

    let response = await fetch(`http://127.0.0.1:5000/employee`, {
        method: "POST",
        body: JSON.stringify({
            username: username ,
            password: password
            
        })
    });


    let responseData = await response.json();
    console.log(responseData)
    if(responseData.employeeID > 0){
        sessionStorage.setItem("value", responseData.employeeID)
        window.location.href = "employee_dashboard.html";
    }else{
        alert('Wrong UserName and/or Password!')
    }



}

let loginForm2 = document.getElementById("login-form2")


loginForm2.onsubmit = async function(e){
    e.preventDefault();
    let username2 = document.getElementById("username2").value;
    let password2 = document.getElementById("password2").value;
    console.log(username2, password2)
    

    let response2 = await fetch(`http://127.0.0.1:5000/manager`, {
        method: "POST",
        body: JSON.stringify({
            username: username2 ,
            password: password2
            
        })
    });


    let responseData2 = await response2.json();
    console.log(responseData2)
    if(responseData2.managerId > 0){
        sessionStorage.setItem("value1", responseData2.managerId)
        window.location.href = "manager_dashboard.html";
    }else{
        alert('Wrong UserName and/or Password!')
    }


}

