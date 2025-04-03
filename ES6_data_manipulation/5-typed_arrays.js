/* eslint-disable */
export default function createInt8TypedArray(length, position, value) {
	if (position >= length) {
	  throw new Error('Position outside range');
	}
	const buffer = new ArrayBuffer(length);
	const view = new DataView(buffer);
	try {
	  view.setInt8(position, value);
	  return view;
	} catch (e) {
	  throw new Error('Position outside range');
	}
  }
