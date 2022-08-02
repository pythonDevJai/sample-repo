
@app.route('/get_all_records' , methods = ['GET'])
def getAllRecords():
    result = session.query(ProductEnquiry).all()
    convertDict = [item.__dict__ for item in result]
    for item in convertDict:
        del item['_sa_instance_state']

    return json.dumps(convertDict)


@app.route('/getSingleRecord' , methods = ['GET'])
def get_single_record():
    request_customer_name = request.args.get('name')
    result = session.query(ProductEnquiry).filter(ProductEnquiry.customerName == request_customer_name).all()
    convert_dict = [item.__dict__ for item in result]
    for item in convert_dict:
        del item['_sa_instance_state']

    return json.dumps(convert_dict)


@app.route('/getMultiRecords' , methods = ['GET'])
def getMultiRecords():
    request_customer_name = request.args.get('name')
    request_dealer_code = request.args.get('code')
    result = session.query(ProductEnquiry , Dealer).filter(ProductEnquiry.customerName == request_customer_name) and \
             (Dealer.dealerCode == request_dealer_code).all()
    convert_dict = [item.__dict__ for item in result]
    for item in convert_dict:
        del item['_sa_instance_state']

    return json.dumps(convert_dict)


@app.route('/getstartswithRecords' , methods = ['GET'])
def getstartswithRecords():
    request_customer_mobile = request.args.get('mobile')
    result = session.query(ProductEnquiry).filter(ProductEnquiry.mobileNumber.like(request_customer_mobile + '%')).all()
    convert_to_dict = [item.__dict__ for item in result]
    for item in convert_to_dict:
        del item['_sa_instance_state']

    return json.dumps(convert_to_dict)


@app.route('/endswithRecords' , methods = ['GET'])
def getendswithRecords():
    request_customer_name = request.args.get('name')
    result = session.query(ProductEnquiry).filter(ProductEnquiry.customerName.like('%' + request_customer_name)).all()
    convert_to_dict = [item.__dict__ for item in result]
    for item in convert_to_dict:

        del item['_sa_instance_state']

    return json.dumps(convert_to_dict)




@app.route('/containsRecords' , methods = ['GET'])
def getcontainsRecords():
    request_customer_number = request.args.get('name')
    result = session.query(ProductEnquiry).filter(ProductEnquiry.customerName.like('%' + request_customer_number + '%')).all()
    convert_to_dict = [item.__dict__ for item in result]
    for item in convert_to_dict:
        del item['_sa_instance_state']
    return json.dumps(convert_to_dict)


@app.route('/updateRecord' , methods = ['PATCH'])
def update_record():
    request_name = request.args.get('name')
    update_vehicle_model = request.args.get('model')
    result = session.query(ProductEnquiry).filter(ProductEnquiry.customerName == request_name).\
             update({'vehicleModel' : update_vehicle_model})
    session.commit()
    return "Records Updated Successfull"


# POST Service
@app.route('/post_record', methods=['POST'])
def postRecords():
    try:
        request_body = request.get_json(force=True)
        for index, item in enumerate(request_body):
            record = ProductEnquiry(customerName=item["customer_name"],
                                    mobileNumber=item["mob_no"],
                                    email=item["email"],
                                    createdDate = datetime.now(),
                                    dealerName = item["dealer_name"],
                                    vehicleModel=item["vehicle_model"],
                                    state = item["state"],
                                    district = item["district"],
                                    city = item["city"],
                                    existingVehicle = item["existing_vehicle"],
                                    wantTestDrive = item["want_to_take_a_test_ride"],
                                    dealerState = item["dealer_state"],
                                    dealerTown = item["dealer_town"],
                                    dealerCode = item["dealer_code"],
                                    briefAboutEnquery = item["brief_about_enquiry"],
                                    expectedDateOfPurchase = item["expected_date_of_purchase"],
                                    intendedUsage = item["intended_usage"],
                                    age = item["age"],
                                    gender = item["gender"],
                                    occupation = item["occupation"],
                                    isProcessed = item["is_processed"])
            session.add_all([record])
        session.commit()
        return "Records Inserted successfully"
    except Exception as err:
        session.rollback()
        print("ERROR IS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",err)
        return "data not inserted"
    finally:
        session.close()


    


@app.route('/put_record', methods=['PUT'])
def putRecord():
    request_body = request.get_json(force=True)
    try:
        result = session.query(ProductEnquiry).filter(ProductEnquiry.\
            mobileNumber==ProductEnquiry(request_body[0]["mobile_number"]))\
            .update(record=ProductEnquiry(request_body[0]["comments"]))
        session.commit()
        return  str(result)
    finally:
        session.close()




@app.route('/getAllRecords' , methods = ['GET'])
def get_all_records():
    req_user_name = request.args.get('username')
    req_password = request.args.get('password')
    req_dealercode = request.args.get('code')

    #req_dealer_code = request.args.get('dealercode')
    try:
        user_result = session.query(Credential).filter(Credential.userName == req_user_name).\
            filter(Credential.passWord == req_password).all()
        #dealer_result = session.query()

    except Exception as err:
        session.rollback()
        print ("err ----> ", err)
        return "error in login page"

    if user_result:
        print("i am inside if --------")
        try:
            dealer_result = session.query(Dealer).filter(Dealer.dealerCode == req_dealercode).all()
        except Exception as err:
            print("error 01 -----> ", err)

    else:
        return "dealer code not found"

    if dealer_result:
        try:
            pe_result = session.query(ProductEnquiry).all()
            convert_dict = [item.__dict__ for item in pe_result]
            for item in convert_dict:
                del item['_sa_instance_state']

            return json.dumps(convert_dict)

        except Exception as err:
            session.rollback()

        finally:
            session.close()

    else:
        return "unauthorized access"

app.run(debug = False)
