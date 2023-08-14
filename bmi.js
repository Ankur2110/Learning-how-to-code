function BMI_Calculator() {
	var weight = document.getElementById('weight').value
	var height = document.getElementById('height').value
	weight = parseFloat(weight);
	height = parseFloat(height);

heightinMeters = height/100



	var BMI = (weight)/(heightinMeters* heightinMeters)
document.getElementById("result").innerHTML = "Your  BMI is " + BMI.toFixed(2)

BMI = parseFloat(BMI)

console.log(BMI)

if (BMI< 18.5) {
  document.getElementById("result2").style.color = "red"
	document.getElementById("result2").innerHTML = "You are underweight!"
}

if (BMI>18.5 && BMI<24.9) {
	  document.getElementById("result2").style.color = "green"
	document.getElementById("result2").innerHTML = "You have normal weight :)"
}

if (BMI>25 && BMI<29.9) {
	  document.getElementById("result2").style.color = "red"
	document.getElementById("result2").innerHTML = "You are overweight"

}

if (BMI>30  && BMI<34.9) {
	  document.getElementById("result2").style.color = "red"
	document.getElementById("result2").innerHTML = "You are in obesity class I!"

}

if (BMI>35 && BMI<39) {
  document.getElementById("result2").style.color = "red"
	document.getElementById("result2").innerHTML = "You are in obesity class II!!"


}


if (BMI>40) {
	  document.getElementById("result2").style.color = "red"
	document.getElementById("result2").innerHTML = "You are in obesity class III!!"

}


}