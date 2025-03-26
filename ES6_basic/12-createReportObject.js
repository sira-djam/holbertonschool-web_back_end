export default function createReportObject(employeesList) {
	// Retourner l'objet avec 'allEmployees' et une méthode 'getNumberOfDepartments'
	return {
	  allEmployees: employeesList, // Contient tous les départements et les employés
	  getNumberOfDepartments: function() {
		// Utilise 'Object.keys' pour obtenir un tableau des clés (départements) et retourne la longueur
		return Object.keys(this.allEmployees).length;
	  }
	};
  }
