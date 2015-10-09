/*
** Copyright (C) 2015 Piotr Pokora <piotrek.pokora@gmail.com>
*/

namespace Diabet {

	public interface Manager : GLib.Object  {

		/**
		 * Get the PersonManager.
		 * 
		 * @param void
		 *
		 * @return {@link PersonManager} instance
		 * 
		 * @throws DiabetException if error occurs
		 */
		public abstract PersonManager get_person_manager() throws DiabetException;

		/**
		 * Get the BolusManager.
		 *
		 * @param void
		 *
		 * @return {@link BolusManager} instance
		 *
		 * @throws DiabetException if error occurs
		 */
		public abstract BolusManager  get_bolus_manager();

		/**
		 * Get the BolusHistoryManager
		 * 
		 * @param void
		 *
		 * @return {@link BolusManager} instance
		 *
		 * @throws DiabetException if error occurs
		 */
		public abstract BolusHistoryManager get_bolus_history_manager();
	}
}
