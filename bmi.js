function BMI_Calculator() {
	var weight = document.getElementById('weight').value
	var height = document.getElementById('height').value
	weight = parseFloat(weight);
	height = parseFloat(height);

heightinMeters = height/100



	var BMI = (weight)/(heightinMeters* heightinMeters)
document.getElementById("result").innerHTML = "Your  BMI is " + BMI.toFixed(2)

}