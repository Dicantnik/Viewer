const MakeForm = document.getElementById("make_form")
const JoinForm = document.getElementById("join_form")
const AddButton = document.getElementById("addroom")
const JoinButton = document.getElementById("joinroom")
const CloseButtonList = document.querySelectorAll('.close')
AddButton.addEventListener('click', () =>{
    console.log(!JoinForm.classList.contains('form2'))
    if (JoinForm.classList.contains('form2')){
        MakeForm.classList.toggle('form1')
    }
})

JoinButton.addEventListener('click', () =>{
    if (MakeForm.classList.contains('form1')){
        JoinForm.classList.toggle('form2')
    }    
})

CloseButtonList.forEach(CloseButton => {
        CloseButton.addEventListener('click', () =>{
        if (!MakeForm.classList.contains('form1')){
            MakeForm.classList.toggle('form1')
        }
        if (!JoinForm.classList.contains('form2')){
            JoinForm.classList.toggle('form2')
        }
    });
})