function signup(){
    if (validateSignupData()) {
        $.ajax({
                type: 'POST',
                url: '/employee/signup/',
                data:  $('#register').serialize(),
                success: function(response){
                    if (response.success == 'true'){
                        alert('Data successfully saved.');
                        location.href = '/'
                    }
                    else if (response.success == 'exist'){
                        alert('User Already Exist.');
                        location.href = '/'
                    }
                    else if (response.success == 'taken'){
                        alert('Username Already Taken.');
                        location.href = '/'
                    }
                    else if (response.success == 'password'){
                        alert('Please Enter Correct Password.');
                        location.href = '/'
                    }
                    else{
                        alert('Sorry for inconvenience, an error occurred');
                    }
                },
        });
    }
}

//     signup form validations start here
function check_user_name(user_name) {
    if ($('#user_name').val() == '') {
        $(user_name_error).css("display", "block");
        $(user_name_error).text("Please enter user name");
        return false;
    } else {
        $(user_name_error).css("display", "none");
        return true;
    }
}

function check_first_name(first_name) {
		if ($('#first_name').val() == '') {
			$(first_name_error).css("display", "block");
			$(first_name_error).text("Please enter first name");
			return false;
		} else {
			$(first_name_error).css("display", "none");
			return true;
		}
	}

function check_last_name(last_name) {
    if ($('#last_name').val() == '') {
        $(last_name_error).css("display", "block");
        $(last_name_error).text("Please enter last name");
        return false;
    } else {
        $(last_name_error).css("display", "none");
        return true;
    }
}

function check_email(email) {
    if ($('#email').val() == '') {
        $(email_error).css("display", "block");
        $(email_error).text("Please enter email");
        return false;
    } else {
        $(email_error).css("display", "none");
        return true;
    }
}

function check_department(department) {
    if ($('#department').val() == '') {
        $(department_error).css("display", "block");
        $(department_error).text("Please enter department");
        return false;
    } else {
        $(department_error).css("display", "none");
        return true;
    }
}

function check_password1(password1) {
    if ($('#password1').val() == '') {
        $(password1_error).css("display", "block");
        $(password1_error).text("Please enter password");
        return false;
    } else {
        $(password1_error).css("display", "none");
        return true;
    }
}

function check_password2(password2) {
    if ($('#password2').val() == '') {
        $(password2_error).css("display", "block");
        $(password2_error).text("Please enter confirm password");
        return false;
    } else {
        $(password2_error).css("display", "none");
        return true;
    }
}

function validateSignupData() {
    if (check_user_name("#user_name") & check_first_name("#first_name") & check_last_name("#last_name") &
        check_email("#email") & check_department("#department") & check_password1("#password1") & check_password2("#password2")){
        return true;
    }
    return false;
}
//  signup validations ends here



function login_c(){
    if (validateLoginData()) {
        $.ajax({
                type: 'POST',
                url: '/employee/login/',
                data:  $('#login').serialize(),
                success: function(response){
                    if (response.success == 'valid'){
                        location.href = '/'
                    }
                    else{
                        alert('Sorry for inconvenience, an error occurred');
                    }
                },
        });
    }
}

//    login form validations start here
function check_username(username) {
    if ($('#username').val() == '') {
        $(username_error).css("display", "block");
        $(username_error).text("Please enter username");
        return false;
    } else {
        $(username_error).css("display", "none");
        return true;
    }
}

function check_password(password) {
    if ($('#password').val() == '') {
        $(password_error).css("display", "block");
        $(password_error).text("Please enter password");
        return false;
    } else {
        $(password_error).css("display", "none");
        return true;
    }
}


function validateLoginData() {
    if (check_username("#username") & check_password("#password")){
        return true;
    }
    return false;
}

//  login validations ends here

function logout(){
    $.ajax({
            type: 'POST',
            url: '/employee/logout/',
            data:  $('#login').serialize(),
            success: function(response){
                if (response.success == 'true'){
                    location.href = '/'
                }
                else{
                    alert('Sorry for inconvenience, an error occurred');
                }
            },
    });

}


function emp_register_c(){
    if (validateRegisterData()) {
        $.ajax({
                type: 'POST',
                url: '/employee/employee/',
                data:  $('#emp_register').serialize(),
                success: function(response){
                    if (response.success == 'true'){
                        alert('Employee Registered.');
                        location.href = '/employee/employee-details/'
                    }
                    else if (response.success == 'exist'){
                        alert('User Already Exist.');
                        location.href = '/employee/employee-registration/'
                    }
                    else{
                        alert('Sorry for inconvenience, an error occurred');
                    }
                },
        });
    }
}

//     Registration form validations start here

function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

function checkrfirstname(first_name) {
		if ($('#first_name').val() == '') {
			$(firstname_error).css("display", "block");
			$(firstname_error).text("Please enter first name");
			return false;
		} else {
			$(firstname_error).css("display", "none");
			return true;
		}
	}

function checkrlastname(last_name) {
    if ($('#last_name').val() == '') {
        $(lastname_error).css("display", "block");
        $(lastname_error).text("Please enter last name");
        return false;
    } else {
        $(lastname_error).css("display", "none");
        return true;
    }
}

function checkremail(email) {
    if ($('#email').val() == '') {
        $(email_error).css("display", "block");
        $(email_error).text("Please enter email");
        return false;
    } else {
        $(email_error).css("display", "none");
        return true;
    }
}

function checkrdepartrment(department) {
    if ($('#department').val() == '') {
        $(department_error).css("display", "block");
        $(department_error).text("Please enter department");
        return false;
    } else {
        $(department_error).css("display", "none");
        return true;
    }
}

function checkrcity(city) {
    if ($('#city').val() == '') {
        $(city_error).css("display", "block");
        $(city_error).text("Please enter city");
        return false;
    } else {
        $(city_error).css("display", "none");
        return true;
    }
}

function checkrmobile(mobbile) {
    if ($('#mobile').val() == '') {
        $(mobile_error).css("display", "block");
        $(mobile_error).text("Please enter mobile");
        return false;
    } else {
        $(mobile_error).css("display", "none");
        return true;
    }
}

function validateRegisterData() {
    if (checkrfirstname("#first_name") & checkrlastname("#last_name") &
        checkremail("#email") & checkrdepartrment("#department") & checkrmobile("#mobilr") & checkrcity("#city")){
        return true;
    }
    return false;
}

//  registration validations ends here


function update(){
    var emp_id = $("#emp_id").val();
    if (validateRegisterData()) {
        $.ajax({
                type: 'POST',
                url: '/employee/update-employee/',
                data:  $('#emp_update').serialize(),
                success: function(response){
                    if (response.success == 'true'){
                        alert('Updated.');
                        location.href = '/employee/employee-details/'
                    }
                    else{
                        alert('Sorry for inconvenience, an error occurred');
                    }
                },
        });
    }
}



function del_emp(){
    var emp_id = $("#emp_id").val();
    $.ajax({
            type: 'POST',
            url: '/employee/delete-employee/',
            data:  $('#emp_update').serialize(),
            success: function(response){
                if (response.success == 'true'){
                    alert('Deleted.');
                    location.href = '/employee/employee-details/'
                }
                else{
                    alert('Sorry for inconvenience, an error occurred');
                }
            },
    });

}


