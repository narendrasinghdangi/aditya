import os
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

from .log_utils import setup_logger

logger = setup_logger(__name__)

current_dir = os.getcwd()
GOOGLE_SHEET_PATH = os.path.join(current_dir, 'backend/google_sheet.json')

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def get_google_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEET_PATH, scope)
    client = gspread.authorize(creds)
    sheet = client.open("facebook_agent_prompt").sheet1
    return sheet

def read_data():
    logger.info("Reading data from CSV.")
    sheet = get_google_sheet()
    df = get_as_dataframe(sheet, evaluate_formulas=True)
   # print(df)
    return df

def write_data(username, password, success=True, error=None):
    logger.info("Writing data to CSV.")
    sheet = get_google_sheet()
    df = get_as_dataframe(sheet, evaluate_formulas=True)
    new_row = {col: "" for col in df.columns}
    new_row["username"] = username
    new_row["password"] = password
    new_row["status"] = "done" if success else error
    df.loc[len(df)] = new_row
    # Save back to CSV
    set_with_dataframe(sheet, df)
    logger.info(f"Updated row with status 'done'.")
    return

if __name__ == "__main__":
    read_data()