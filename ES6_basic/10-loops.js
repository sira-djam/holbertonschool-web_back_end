export default function appendToEachArrayValue(array, appendString) {
	// Utilisation de 'let' ou 'const' au lieu de 'var'
	let idx = 0;
	for (const value of array) {
	  // Utilisation de 'let' pour indexer, ou simplement incrémentation de 'idx'
	  array[idx] = appendString + value;
	  idx++;
	}

	return array;
  }
