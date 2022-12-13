# ================== Hotel Reservation (Quote Generator) ===================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

# Colors
textPrimary = "#ffffff"
bgPrimary = "#ffffff"
borderColor = "#d8d8d8"
highlightcolor= "#6366F1"

# Locations Options
locationOptions = {'Belfast': [
                        'Belfast City Centre',
                        'Crowne Plaza',
                        'Indigo Hotel',
                        'Regent Hotel',
                        'Atwell Suite'
                        ],
                   'Cork': [
                        'Jurys Inn Cork',
                        'Clayton Hotel',
                        'Rachestown Park Hotel',
                        'Radisson Blue Hotel',
                        'Imperial Hotel',
                        'Oriel House Hotel'
                        ],
                    'Dublin': [
                        'Jurys Inn Cork',
                        'Clayton Hotel',
                        'Rachestown Park Hotel',
                        'Radisson Blue Hotel',
                        'Imperial Hotel',
                        'Oriel House Hotel',
                        'The Kingsley Hotel',
                        'Cork International Hotel',
                        'Gabriel House'
                    ],
                    'Galway':[
                        'Maldron Hotel',
                        'The Eyre Square',
                        'The Huntsman Inn',
                        'Menlo Park Hotel',
                        'The Victoria Hotel'
                    ],
                    'Limerick':[
                        'George Limerick Hotel',
                        'The Bedford Townhouse',
                        'Maldron Hotel',
                        'Clayton Hotel',
                        'Limerick City Hotel',
                        'Radisson Blue Hotel'
                    ],
                    'Waterford':[
                        'Dooleys Hotel',
                        'The Fitzwilton Hotel',
                        'Waterford Marina hotel',
                        'Diamond Hill Country House'
                    ]
}

class AdminControls():
    def __init__(self):
        self.root = Tk()
        self.items = []

        # Local Variables
        self.strName = StringVar()
        self.strEmail = StringVar()
        self.strAddress = StringVar()
        self.strTown = StringVar()
        self.strCounty = StringVar()
        self.strTelephone = IntVar()
        self.strPayment = StringVar()
        self.strLocation = StringVar(value='Select Location')
        self.strModelChoiceHotel = StringVar(value='Select Hotel')
        self.strNights = IntVar()
        self.strExtras = StringVar()
        self.strBillPrice = DoubleVar()
        self.strBillExtras = DoubleVar()
        self.strBillSubTotal = DoubleVar()
        self.strBillVAT = DoubleVar()
        self.strBillTotal = DoubleVar()

        # Function Declaration
        self.admin_control_frame()
        self.hotel_control_frame()
        self.bill_information()

    # Updating the fild Choice Hotel
    def get_update_data(self, event):
        self.combomodelChoiceHotel['values'] = locationOptions[self.combovehotelLocation.get()]

    def admin_control_frame(self):

        # Setup Frame
        self.entriesFrame = Frame(self.root, width=700, bg=bgPrimary)
        self.entriesFrame.pack(anchor=W, fill=BOTH, expand=FALSE, side=LEFT,padx=20)

        # Main Title
        self.admin_frame_title = Label(self.entriesFrame,
                                       text="Customer Details",
                                       font=("Arial", 14), bg=bgPrimary)
        self.admin_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        # Customer Name
        self.customerName = Label(self.entriesFrame, text="Client/Company Name",
                                  font=("Arial", 10),
                                  bg=bgPrimary)
        self.customerName.grid(row=1, column=0, padx=10, sticky="w")
        self.txtCustomerName = Entry(self.entriesFrame, textvariable=self.strName, width=30, border=0,
                                     font=("Arial", 10), highlightthickness=2)
        self.txtCustomerName.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtCustomerName.grid(row=1, column=1, padx=10, pady=10)

        # Customer Email
        self.customerEmail = Label(self.entriesFrame, text="Email",
                                  font=("Arial", 10),
                                  bg=bgPrimary)
        self.customerEmail.grid(row=1, column=2, padx=10, sticky="w")
        self.txtCustomerEmail = Entry(self.entriesFrame, textvariable=self.strEmail, width=30, border=0,
                                     font=("Arial", 10), highlightthickness=2)
        self.txtCustomerEmail.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtCustomerEmail.grid(row=1, column=3, padx=10, pady=10)

        # Customer Street Address
        self.customerStreet = Label(self.entriesFrame, text="Address",
                                    font=("Arial", 10),
                                    bg=bgPrimary)
        self.customerStreet.grid(row=2, column=0, padx=10, sticky="w")
        self.txtCustomerStreet = Entry(self.entriesFrame,textvariable=self.strAddress, width=30, border=0,
                                       font=("Arial", 10), highlightthickness=2)
        self.txtCustomerStreet.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtCustomerStreet.grid(row=2, column=1, padx=10, pady=10)

        # Contact Telephone Number
        self.contactNumber = Label(self.entriesFrame, text="Phone Number",
                                    font=("Arial", 10),
                                   bg=bgPrimary)
        self.contactNumber.grid(row=2, column=2, padx=10, sticky="w")
        self.txtcontactNumber = Entry(self.entriesFrame, textvariable=self.strTelephone, width=30, border=0,
                                       font=("Arial", 10), highlightthickness=2)
        self.txtcontactNumber.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtcontactNumber.grid(row=2, column=3, padx=10, pady=10)

        # Customer Town/City
        self.customerCity = Label(self.entriesFrame, text="City",
                                    font=("Arial", 10),
                                    bg=bgPrimary)
        self.customerCity.grid(row=3, column=0, padx=10, sticky="w")
        self.txtCustomerCity = Entry(self.entriesFrame, textvariable=self.strTown, width=30, border=0,
                                     font=("Arial", 10), highlightthickness=2)
        self.txtCustomerCity.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtCustomerCity.grid(row=3, column=1, padx=10, pady=10)

        # Customer County
        self.customerCounty = Label(self.entriesFrame, text="Country",
                                    font=("Arial", 10),
                                    bg=bgPrimary)
        self.customerCounty.grid(row=3, column=2, padx=10, sticky="w")
        self.txtCustomerCounty = Entry(self.entriesFrame, textvariable=self.strCounty, width=30, border=0,
                                     font=("Arial", 10), highlightthickness=2)
        self.txtCustomerCounty.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtCustomerCounty.grid(row=3, column=3, padx=10, pady=10)


        # Selection of Payment Type
        self.paymentType = Label(self.entriesFrame, text="Payment Type",
                                   font=("Arial", 10),
                                    bg=bgPrimary)
        self.paymentType.grid(row=4, column=0, padx=10, sticky="w")
        self.combopaymentType = ttk.Combobox(self.entriesFrame, textvariable=self.strPayment, width=28,
                                        font=("Arial", 10),
                                        state="readonly")
        self.combopaymentType['values'] = ("Cash", "Mastercad", "Visa")
        self.combopaymentType.grid(row=4, column=1, padx=10, pady=1)



    def hotel_control_frame(self):

        # Main Title
        self.hotel_frame_title = Label(self.entriesFrame,
                                       text="Reservation Details",
                                       font=("Arial", 14), bg=bgPrimary)
        self.hotel_frame_title.grid(row=5, columnspan=2, padx=10, pady=20, sticky="w")

        # Hotel Location
        self.hotel_location = Label(self.entriesFrame, text="Location",
                                    font=("Arial", 10),
                                    bg=bgPrimary)
        self.hotel_location.grid(row=6, column=0, padx=10, sticky="w")
        self.combovehotelLocation = ttk.Combobox(self.entriesFrame, textvariable=self.strLocation, width=28,
                                    font=("Arial", 10),
                                    state="readonly")
        self.combovehotelLocation['values'] = list(locationOptions.keys())
        self.combovehotelLocation.bind('<<ComboboxSelected>>', self.get_update_data)
        self.combovehotelLocation.grid(row=6, column=1, padx=10, pady=1)

        # Choose Hotel
        self.modelChoiceHotel = Label(self.entriesFrame, text="Hotel",
                                font=("Arial", 10),
                                bg=bgPrimary)
        self.modelChoiceHotel.grid(row=6, column=2, padx=10, sticky="w")
        self.combomodelChoiceHotel = ttk.Combobox(self.entriesFrame, textvariable=self.strModelChoiceHotel, width=28,
                                        font=("Arial", 10),
                                        state="readonly")
        self.combomodelChoiceHotel.grid(row=6, column=3, padx=10, pady=10, sticky="w")

        # Nights
        self.nights = Label(self.entriesFrame, text="Nights",
                            font=("Arial", 10),
                          bg=bgPrimary)
        self.nights.grid(row=7, column=0, padx=10, sticky="w")
        self.txtDays = Entry(self.entriesFrame, textvariable=self.strNights, width=30, border=0,
                                       font=("Arial", 10), highlightthickness=2)
        self.txtDays.config(highlightbackground=borderColor, highlightcolor=highlightcolor)
        self.txtDays.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # Extras
        self.extras = Label(self.entriesFrame, text="Extras",
                                   font=("Arial", 10),
                            bg=bgPrimary)
        self.extras.grid(row=7, column=2, padx=10, sticky="w")
        self.comboExtras = ttk.Combobox(self.entriesFrame, textvariable=self.strExtras, width=28,
                                               font=("Arial", 10),
                                               state="readonly")
        self.comboExtras['values'] = 'list(extras.keys())'
        self.comboExtras.grid(row=7, column=3, padx=10, pady=10, sticky="w")

    def bill_information(self):
        self.billFrame = Frame(self.root, bg='yellow')
        self.billFrame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)

app = AdminControls()

app.root.title("Hotel Reservation")
app.root.geometry("1200x700")
app.root.mainloop()

