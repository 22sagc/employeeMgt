function signup(){
    $.ajax({
            type: 'POST',
            url: '/employee/register/',
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

function login_c(){
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
    $.ajax({
            type: 'POST',
            url: '/employee/save-employee/',
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
                else if (response.success == 'null'){
                    alert('Please Insert ALl Data.');
                    location.href = '/employee/employee-registration/'
                }
                else{
                    alert('Sorry for inconvenience, an error occurred');
                }
            },
    });

}

function update(){
    var emp_id = $("#emp_id").val();
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