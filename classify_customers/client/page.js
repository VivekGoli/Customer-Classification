function onPageload(){
    console.log("page loaded");
    var url="http://127.0.0.1:5000/dummy";
    $.get(url);
}

function onClickPredict(){
    console.log("customer category prediction");

    var sex=document.getElementById("Gender");
    var married=document.getElementById("Ever_Married");
    var age=document.getElementById("Age");
    var graduation=document.getElementById("Graduated");
    var profession=document.getElementById("Profession");
    var experience=document.getElementById("Work_Experience");
    var score=document.getElementById("Spending_Score");
    var family=document.getElementById("Family_Size");
    var var1=document.getElementById("Var_1");
    var pred=document.getElementById('prediction');

    console.log(married.value, profession.value)
    var url="http://127.0.0.1:5000/predict"

    $.post(url,{
        Gender: parseInt(sex.value),
        Ever_Married: parseInt(married.value),
        Age: parseInt(age.value),
        Graduated: parseInt(graduation.value),
        Profession: parseInt(profession.value),
        Work_Experience: parseFloat(experience.value),
        Spending_Score: parseInt(score.value),
        Family_Size: parseFloat(family.value),
        Var_1: parseInt(var1.value)
    }, function(data, status){
        console.log(data.prediction);
        pred.innerHTML="<h4>"+data.prediction.toString()+"</h4>"
        console.log(status)
    })
}

window.onload=onPageload;