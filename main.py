# ================== Hotel Reservation (Quote Generator) ===================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
hotelPrice = {'Belfast': {'day': 37.50, 'week': 236.50, 'fort': 448.90},
              'Cork': {'day': 43.25, 'week': 272.48, 'fort': 517.70},
              'Dublin': {'day': 49.70, 'week': 313.11, 'fort': 594.91},
              'Galway': {'day': 55.30, 'week': 348.39, 'fort': 661.95},
              'Limerick': {'day': 63.15, 'week': 397.85, 'fort': 755.92},
              'Waterford': {'day': 35.10, 'week': 221.13, 'fort': 420.15}
              }

# Extra Options
extras = {'No Extras': {'rate': 0},
          'Internet Service': {'rate': 22},
          'Jacuzzi': {'rate': 78},
          'Gym': {'rate': 7}
          }


class AdminControls():
    def __init__(self):
        self.root = Tk()


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
        self.price_list()

    # Updating the fild Choice Hotel
    def get_update_data(self, event):
        self.combomodelChoiceHotel['values'] = locationOptions[self.combohotelLocation.get()]

    def admin_control_frame(self):

        # Setup Frame
        self.entriesFrame = Frame(self.root, width=700, bg=bgPrimary)
        self.entriesFrame.pack(anchor=W, fill=BOTH, expand=FALSE, side=LEFT, padx=10, pady=10)

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
        self.txtCustomerEmail = Entry(self.entriesFrame, textvariable=self.strEmail, width=25, border=0,
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
        self.txtcontactNumber = Entry(self.entriesFrame, textvariable=self.strTelephone, width=25, border=0,
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
        self.txtCustomerCounty = Entry(self.entriesFrame, textvariable=self.strCounty, width=25, border=0,
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
        self.hotel_frame_title.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

        # Hotel Location
        self.hotel_location = Label(self.entriesFrame, text="Location",
                                    font=("Arial", 10),
                                    bg=bgPrimary)
        self.hotel_location.grid(row=6, column=0, padx=10, sticky="w")
        self.combohotelLocation = ttk.Combobox(self.entriesFrame, textvariable=self.strLocation, width=28,
                                    font=("Arial", 10),
                                    state="readonly")
        self.combohotelLocation['values'] = list(locationOptions.keys())
        self.combohotelLocation.bind('<<ComboboxSelected>>', self.get_update_data)
        self.combohotelLocation.grid(row=6, column=1, padx=10, pady=1)

        # Choose Hotel
        self.modelChoiceHotel = Label(self.entriesFrame, text="Hotel",
                                font=("Arial", 10),
                                bg=bgPrimary)
        self.modelChoiceHotel.grid(row=6, column=2, padx=10, sticky="w")
        self.combomodelChoiceHotel = ttk.Combobox(self.entriesFrame, textvariable=self.strModelChoiceHotel, width=23,
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
        self.comboExtras = ttk.Combobox(self.entriesFrame, textvariable=self.strExtras, width=23,
                                               font=("Arial", 10),
                                               state="readonly")
        self.comboExtras['values'] = list(extras.keys())
        self.comboExtras.grid(row=7, column=3, padx=10, pady=10, sticky="w")

        self.btnAdd = Button(self.entriesFrame, text="Calculate",
                             command=self.addItems,
                             width=20,
                             border=0,
                             bg="#7F19E6",
                             fg=textPrimary,
                             font=("Arial", 12))
        self.btnAdd.grid(row=8, column=2, padx=10, pady=20, sticky=E)

        self.btnClean = Button(self.entriesFrame, text="Clean",
                               command=self.resetForm,
                               width=20,
                               border=0,
                               bg="#5C6370",
                               fg=textPrimary,
                               font=("Arial", 12))
        self.btnClean.grid(row=8, column=3, padx=10, pady=20, sticky=W)

    # Section for the billing
    def bill_information(self):
        self.billFrame = Frame(self.root, bg=bgPrimary)
        self.billFrame.pack(anchor=W, fill=BOTH, expand=FALSE, side=RIGHT, padx=10, pady=10)

        # Title Section Bill
        self.txtBillTitle = Label(self.billFrame, text="Quotation",
                              font=("Arial", 16),
                                  bg=bgPrimary)
        self.txtBillTitle.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.txtBillTitle = Label(self.billFrame, text="#001",
                                  font=("Arial", 16),
                                  bg=bgPrimary)
        self.txtBillTitle.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        # Separator
        self.borderOne = ttk.Separator(self.billFrame, orient="horizontal")
        self.borderOne.grid(row=1, column=0, columnspan=99, ipadx=200)

        # Information Customer
        self.txtBillClientNameTitle = Label(self.billFrame, text="Client:",
                                      font=("Arial", 8),
                                      bg=bgPrimary)
        self.txtBillClientNameTitle.grid(row=2, column=0, sticky="e")
        self.txtBillClientName = Label(self.billFrame, textvariable=self.strName, width=30,
                                   font=("Arial", 8),
                                   bg=bgPrimary)
        self.txtBillClientName.grid(row=2, column=1, sticky="w")

        self.txtBillClientEmailTitle = Label(self.billFrame, text="Email:",
                                       font=("Arial", 8),
                                       bg=bgPrimary)
        self.txtBillClientEmailTitle.grid(row=3, column=0, sticky="e")
        self.txtBillClientEmail = Label(self.billFrame, textvariable=self.strEmail, width=30,
                                       font=("Arial", 8),
                                       bg=bgPrimary)
        self.txtBillClientEmail.grid(row=3, column=1, sticky="w")

        self.txtBillClientAddressTitle = Label(self.billFrame, text="Address:",
                                        font=("Arial", 8),
                                        bg=bgPrimary)
        self.txtBillClientAddressTitle.grid(row=4, column=0, sticky="e")
        self.txtBillClientAddress = Label(self.billFrame, textvariable=self.strAddress, width=30,
                                        font=("Arial", 8),
                                        bg=bgPrimary)
        self.txtBillClientAddress.grid(row=4, column=1, sticky="w")

        self.txtBillClientPhoneNumberTitle = Label(self.billFrame, text="Phone Number:",
                                        font=("Arial", 8),
                                        bg=bgPrimary)
        self.txtBillClientPhoneNumberTitle.grid(row=5, column=0, sticky="e")
        self.txtBillClientPhoneNumber = Label(self.billFrame, textvariable=self.strTelephone, width=30,
                                          font=("Arial", 8),
                                          bg=bgPrimary)
        self.txtBillClientPhoneNumber.grid(row=5, column=1, sticky="e")

        self.txtBillClientCityTitle = Label(self.billFrame, text="City:",
                                        font=("Arial", 8),
                                        bg=bgPrimary)
        self.txtBillClientCityTitle.grid(row=6, column=0, sticky="e")
        self.txtBillClientCity = Label(self.billFrame, textvariable=self.strTown, width=30,
                                              font=("Arial", 8),
                                              bg=bgPrimary)
        self.txtBillClientCity.grid(row=6, column=1, sticky="w")

        self.txtBillClientCountryTitle = Label(self.billFrame, text="Country:",
                                        font=("Arial", 8),
                                        bg=bgPrimary)
        self.txtBillClientCountryTitle.grid(row=7, column=0, sticky="e")
        self.txtBillClientCountry = Label(self.billFrame, textvariable=self.strCounty, width=30,
                                              font=("Arial", 8),
                                              bg=bgPrimary)
        self.txtBillClientCountry.grid(row=7, column=1, sticky="w")

        self.txtBillClientPaymentTitle = Label(self.billFrame, text="Payment:",
                                        font=("Arial", 8),
                                        bg=bgPrimary)
        self.txtBillClientPaymentTitle.grid(row=8, column=0, sticky="e")
        self.txtBillClientPayment = Label(self.billFrame, textvariable=self.strPayment, width=30,
                                          font=("Arial", 8),
                                          bg=bgPrimary)
        self.txtBillClientPayment.grid(row=8, column=1, sticky="w")

        # Separator
        self.borderTwo = ttk.Separator(self.billFrame, orient="horizontal")
        self.borderTwo.grid(row=9, column=0, columnspan=99, ipadx=200)

        # Sub title Section Bill
        self.txtBillTitle = Label(self.billFrame, text="Badget Required",
                                  font=("Arial", 12),
                                  bg=bgPrimary)
        self.txtBillTitle.grid(row=10, columnspan=2, padx=10, sticky="w")

        # Separator
        self.borderTwo = ttk.Separator(self.billFrame, orient="horizontal")
        self.borderTwo.grid(row=11, column=0, columnspan=99, ipadx=200)

        # Cost Rent Hotel
        self.txtBillCostTitle = Label(self.billFrame, text="Cost ", width=20,
                                font=("Arial", 10), bg=bgPrimary)
        self.txtBillCostTitle.grid(row=12, column=0, pady=10, sticky="w")

        self.txtBillCost = Label(self.billFrame, textvariable=self.strBillPrice, width=20,
                                font=("Arial", 10), bg=bgPrimary)
        self.txtBillCost.grid(row=12, column=1, pady=10, sticky="w")

        # Charge Extras
        self.txtBillExtrasTitle = Label(self.billFrame, text="Extras", width=20,
                                font=("Arial", 10),
                                bg=bgPrimary)
        self.txtBillExtrasTitle.grid(row=13, column=0, sticky="w")

        self.txtBillExtras = Label(self.billFrame, textvariable=self.strBillExtras, width=20,
                                font=("Arial", 10),
                                bg=bgPrimary)
        self.txtBillExtras.grid(row=13, column=1, sticky="w")

        # Sum Sub Total
        self.txtBillSubTotalTitle = Label(self.billFrame, text="Sub Total", width=20,
                              font=("Arial", 10, 'bold'))
        self.txtBillSubTotalTitle.grid(row=14, column=0, pady=10, sticky="w")
        self.txtBillSubTotal = Label(self.billFrame, textvariable=self.strBillSubTotal, width=20,
                              font=("Arial", 10))
        self.txtBillSubTotal.grid(row=14, column=1, pady=10, sticky="w")

        # Calculate VAT
        self.txtBillVatTitle = Label(self.billFrame, text="VAT (23%)", width=20,
                              font=("Arial", 10),bg=bgPrimary)
        self.txtBillVatTitle.grid(row=15, column=0, pady=10, sticky="w")
        self.txtBillVat = Label(self.billFrame, textvariable=self.strBillVAT, width=20,
                              font=("Arial", 10),bg=bgPrimary)
        self.txtBillVat.grid(row=15, column=1, pady=10, sticky="w")

        #Sum Gross Total
        self.txtBillTotalTitle = Label(self.billFrame, text="Total Rental Price", width=20,
                              font=("Arial", 10, 'bold'))
        self.txtBillTotalTitle.grid(row=16, column=0, pady=10, sticky="w")
        self.txtBillTotal = Label(self.billFrame, textvariable=self.strBillTotal, width=20,
                              font=("Arial", 10))
        self.txtBillTotal.grid(row=16, column=1, pady=10, sticky="w")

        # Separator
        self.borderThree = ttk.Separator(self.billFrame, orient="horizontal")
        self.borderThree.grid(row=17, column=0, columnspan=99, ipadx=200)

        # Footer Title Section Bill
        self.txtBillTitle = Label(self.billFrame, text="Thank you!!!",
                                  font=("Arial", 12),
                                  bg=bgPrimary)
        self.txtBillTitle.grid(row=18, columnspan=2, padx=10)

    def price_list(self):

        for location in locationOptions:
            if location == 'Cork':
                for hotel in locationOptions.keys():
                    print(hotel)

        try:
            for location in locationOptions:
                if self.combohotelLocation.get() == location:
                    if self.strNights.get() == 0:
                        self.strBillPrice.set(0.0)
                    elif self.strNights.get() == 1:
                        self.strBillPrice.set(hotelPrice[location]['day'])
                    elif self.strNights.get() in range(2, 8):
                        self.strBillPrice.set(hotelPrice[location]['week'])
                    elif self.strNights.get() in range(8, 14):
                        self.strBillPrice.set(hotelPrice[location]['fort'])
                    elif self.strNights.get() >= 15:
                        self.strBillPrice.set(
                            hotelPrice['Belfast']['fort'] + (
                                    (self.strNights.get() - 14) * hotelPrice[location]['day']))
        except Exception as e:
            print(e)
    # Calculating Sub Total
    def sub_total(self):
        result = self.strBillPrice.get() + self.strBillExtras.get()
        self.strBillSubTotal.set(result)

    # Calculating VAT
    def calculate_vat(self):
        result = self.strBillSubTotal.get() * 0.23
        self.strBillVAT.set(round(result,2))

    # Calculating Gross Total
    def gross_total(self):
        result = self.strBillSubTotal.get() + self.strBillVAT.get()
        self.strBillTotal.set(round(result,2))

    def add_extras(self):

        for extra in extras:
            if self.comboExtras.get() == extra:
                self.strBillExtras.set(extras[self.comboExtras.get()]['rate'])

    # Adding items
    def addItems(self):
        # Valitadion Fields
        if self.combohotelLocation.get() == "Select Location":
            messagebox.showerror("Error!", "Location is Required!")
            return
        elif self.combomodelChoiceHotel.get() == "Select Hotel":
            messagebox.showerror("Error!", "Hotel is Required!")
            return
        elif self.txtDays.get() == "0":
            messagebox.showerror("Error!", "Number of Days is Required!")
            return
        else:
            self.price_list()
            self.add_extras()
            self.sub_total()
            self.calculate_vat()
            self.gross_total()


    # Reset Form
    def resetForm(self):
        self.strName.set("")
        self.strEmail.set("")
        self.strAddress.set("")
        self.strTown.set("")
        self.strCounty.set("")
        self.strTelephone.set(0)
        self.strPayment.set("")
        self.strLocation.set(value='Select Location')
        self.strModelChoiceHotel.set(value='Select Hotel')
        self.strNights.set(0)
        self.strExtras.set("")
        self.strBillPrice.set(0)
        self.strBillExtras.set(0)
        self.strBillSubTotal.set(0)
        self.strBillVAT.set(0)
        self.strBillTotal.set(0)

app = AdminControls()

app.root.title("Hotel Reservation")
app.root.geometry("1200x500")
app.root.config(background="#242424")
app.root.resizable(False, False)
app.root.mainloop()

