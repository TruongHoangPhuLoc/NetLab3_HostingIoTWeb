document.getElementById("F").addEventListener("mousedown",async function(){
    var result = await httpPost("/manual_control","F");
    console.log(result);
})
document.getElementById("F").addEventListener("mouseup",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
// document.getElementById("F").addEventListener("click",function(){
//     var result = httpPost("/manual_control","F");
// })
document.getElementById("L").addEventListener("mousedown",async function(){
    var result = await httpPost("/manual_control","L");
    console.log(result);
})
document.getElementById("L").addEventListener("mouseup",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
document.getElementById("S").addEventListener("click",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
document.getElementById("R").addEventListener("mousedown",async function(){
    var result = await httpPost("/manual_control","R");
    console.log(result);
})
document.getElementById("R").addEventListener("mouseup",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
document.getElementById("B").addEventListener("mousedown",async function(){
    var result = await httpPost("/manual_control","B");
    console.log(result);
})
document.getElementById("B").addEventListener("mouseup",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
// document.getElementById("L").addEventListener("click",function(){
//     var result = httpPost("/manual_control","L");
//     console.log(result);
// })
// document.getElementById("R").addEventListener("click",function(){
//     var result = httpPost("/manual_control","R");
//     console.log(result);
// })
document.getElementById("F").addEventListener("touchstart",async function(){
    var result = await httpPost("/manual_control","F");
    console.log(result);
})
document.getElementById("F").addEventListener("touchend",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
document.getElementById("B").addEventListener("touchstart",async function(){
    var result =  await httpPost("/manual_control","B");
    console.log(result);
})
document.getElementById("B").addEventListener("touchend",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
document.getElementById("L").addEventListener("touchstart",async function(){
    var result = await httpPost("/manual_control","L");
    console.log(result);
})
document.getElementById("L").addEventListener("touchend",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})
document.getElementById("R").addEventListener("touchstart",async function(){
    var result = await httpPost("/manual_control","R");
    console.log(result);
})
document.getElementById("R").addEventListener("touchend",async function(){
    var result = await httpPost("/manual_control","S");
    console.log(result);
})