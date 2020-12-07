function art()
{
	var a = document.getElementById('fval').value;
	// alert(typeof(a))
	var b = document.getElementById('sval').value;
	// alert("Add of "+a+" and "+b+" is: "+(parseInt(a)+parseInt(b))+"\n"+"Sub of "+a+" and "+b+" is: "+(parseInt(a)-parseInt(b)))
	document.getElementById("res").innerText="Add of "+a+" and "+b+" is: "+(parseInt(a)+parseInt(b))+"\n"+"Sub of "+a+" and "+b+" is: "+(parseInt(a)-parseInt(b))
}