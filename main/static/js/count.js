const targetForm= document.querySelector('.jss_content_form')
const counted_text= document.querySelector('.counted_text')

// document는 전체를 말함
//클래스라서 . id는 #
//변수 지정 const a= _값이 안변함 let b=_값이 변함
//console.log(targetForm) _python의 print역할
targetForm.addEventListener("keyup",function(){
    counted_text.innerHTML = targetForm.value.length //글자 길이
})
//이벤트 핸들러_요소.addEventListener("이벤트",이벤트를 감지했을 때 실행되는 함수)