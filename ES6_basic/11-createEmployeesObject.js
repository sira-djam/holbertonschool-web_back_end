export default function createEmployeesObject(departmentName, employees) {
	// Créer un objet où la clé est le nom du département et la valeur est le tableau des employés
	const result = {};
	result[departmentName] = employees;

	return result;
  }
