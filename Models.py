class Xl(Base):
    __tablename__ = "xl"
    customerName = Column("customer_name" , String)
    age          = Column("age" , Integer)
    gender       = Column("gender" , String)
    mobNumber    = Column("mob_no" , Integer , primary_key = True)
    model        = Column("model" , String)
    want_To_Take_Test_Ride = Column("want_to_take_test_ride" , BOOLEAN)
    city         = Column("city" , String)
    district     = Column("district" , String)
    state        = Column("state" , String)


#------------------------------------------------------------------------------


class StudentInfo(Base):
    __tablename__ = 'studentinfo'
    Name = Column("name", String)
    Age = Column("age", Integer)
    Gender = Column("gender", String)
    mobileNumber = Column("mobile_number", Integer, primary_key = True)
    place = Column("place" , String)
    idNo = Column("id_no" , Integer)
    slNo = Column("sl_no" , Integer)
    


#-----------------------------------------------------------------------------------



class Credential(Base):
    __tablename__ = "credential"
    userName = Column("user_name" , String)
    passWord = Column("password" , String , primary_key = True)


#------------------------------------------------------------------------------



class Dealer(Base):
    """ Dealer model which has all details -table names & columns"""
    __tablename__ = "dealer"
    dealerName = Column("dealer_name", String)
    dealerCode = Column("dealer_code", String, primary_key = True)
    dealerstate = Column("dealer_state",String)


#---------------------------------------------------------------------------------


class ProductEnquiry(Base):
    """ Product enquiry form model which has all details -table names & columns"""
    __tablename__ = "productenquiry"
    customerName = Column("customer_name", String)
    dealerName = Column("dealer_name" , String)
    createdDate = Column("created_date", String)
    mobileNumber = Column("mob_no", Integer, primary_key=True)
    email = Column("email", String)
    vehicleModel = Column("vehicle_model",String)
    state = Column("state",String)
    district = Column("district",String)
    city = Column("city",String)
    existingVehicle = Column("existing_vehicle",String)
    wantTestDrive = Column("want_to_take_a_test_ride", BOOLEAN)
    dealerState = Column("dealer_state",String)
    dealerTown = Column("dealer_town",String)
    dealerCode = Column("dealer_code" , String)
    briefAboutEnquery = Column("brief_about_enquiry", String)
    expectedDateOfPurchase = Column("expected_date_of_purchase", String)
    intendedUsage = Column("intended_usage", String)
    age = Column("age" , Integer)
    gender = Column("gender" , String)
    occupation = Column("occupation" , String)
    isNew = Column("is_new" , BOOLEAN)
    feedBack = Column("feed_back" , String)
    sentToDealer = Column("sent_to_dealer" , BOOLEAN)


#------------------------------------------------------------------------------------------


class Checking(Base):

    __tablename__ = "checking"
    Id = Column("id" , Integer)
    name = Column("name" , String)


#---------------------------------------------------------------------------


class Checkk(Base):
    __tablename__ = "checkk"
    Id = Column("id" , Integer)
    SlNo = Column("slno" , Integer)
    name = Column("name" , String)


#---------------------------------------------------------

class CustomerProductEnquiry(Base):

    __tablename__ = "customerproductenquiry"
    customerName = Column("customer_name" , String)
    mobNo = Column("mob_no" , Integer , primary_key = True)
    email = Column("email" , String)
    vehicleModel = Column("vehicle_model" , String)
    state = Column("state" , String)
    district = Column("district" , String)
    city = Column("city" , String)
    existing_vehicle = Column("existing_vehicle" , String)
    wantToTakeATestRide = Column("wnat_to_take_a_test_ride" , String)
    breif_about_enquiry = Column("breif_about_enquiry" , String)
    expected_date_of_purchase = Column("expected_date_of_purchase" , String)
    gender = Column("gender" , String)
    age = Column("age" , Integer)
    occupation = Column("occupation" , String)
    intended_usage = Column("intended_usage" , String)
    created_date = Column("created_date" , String)
    dealer_code = Column("dealer_code" , String)
    dealer_name = Column("dealer_name" , String)
    dealer_state = Column("dealer_state" , String)
    dealer_town = Column("dealer_town" , String)
    error = Column("error" , String)
    is_processed = Column("is_processed" , String)



#-------------------------------------------------------------


class Dummy(Base):
    __tablename__ = "dummy"
    name = Column("name" , String)
    age = Column("age" , Integer)
    mobile_no = Column("mobile_no" , Integer)
    dummyColumn = Column("dummy_column" , BOOLEAN)

#-----------------------------------------------------------------

class CompanyPortal(Base):
    """ Product enquiry form model which has all details -table names & columns"""
    __tablename__ = "company_portal"
    customerName = Column("customer_name", String)
    dealerName = Column("dealer_name" , String)
    createdDate = Column("created_date", String)
    mobileNumber = Column("mob_no", Integer, primary_key=True)
    email = Column("email", String)
    vehicleModel = Column("vehicle_model",String)
    state = Column("state",String)
    district = Column("district",String)
    city = Column("city",String)
    existingVehicle = Column("existing_vehicle",String)
    wantTestDrive = Column("want_to_take_a_test_ride", BOOLEAN)
    dealerState = Column("dealer_state",String)
    dealerTown = Column("dealer_town",String)
    dealerCode = Column("dealer_code" , String)
    briefAboutEnquery = Column("brief_about_enquiry", String)
    expectedDateOfPurchase = Column("expected_date_of_purchase", String)
    intendedUsage = Column("intended_usage", String)
    age = Column("age" , Integer)
    gender = Column("gender" , String)
    occupation = Column("occupation" , String)
    isNew = Column("is_new" , BOOLEAN)
    feedBack = Column("feed_back" , String)
    sentToDealer = Column("sent_to_dealer" , BOOLEAN)
    isNewCustomer = Column("is_new_customer" , BOOLEAN)

    

    
    

