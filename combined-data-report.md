# CSV Consolidatie Rapport

- Outputbestand: `/tmp/workspace/Proowner7/Data-Migratie/combined-data.csv`
- Output delimiter: `;`
- Totaal bronbestanden: `25`
- Totaal doelschema kolommen (excl. source_file): `146`
- Totaal bronrijen: `1032170`
- Totaal samengevoegde rijen: `1032170`
- Validatie rijtelling: `OK`

## Bronbestand overzicht

| Bestand | Encoding | Delimiter | Rijen |
|---|---|---|---:|
| `advisers.csv` | `utf-8-sig` | `,` | 1347 |
| `customer-lead-information.csv` | `utf-8-sig` | `,` | 16437 |
| `customers.csv` | `utf-8-sig` | `,` | 19899 |
| `employees.csv` | `utf-8-sig` | `,` | 168 |
| `inspections.csv` | `utf-8-sig` | `,` | 12194 |
| `installation-requirement-rules.csv` | `utf-8-sig` | `,` | 438 |
| `installation-requirement.csv` | `utf-8-sig` | `,` | 4046 |
| `installations.csv` | `utf-8-sig` | `,` | 2729 |
| `intermediaries.csv` | `utf-8-sig` | `,` | 726 |
| `invoices-lines.csv` | `utf-8-sig` | `,` | 53469 |
| `invoices.csv` | `utf-8-sig` | `,` | 2411 |
| `order-event-logs.csv` | `utf-8-sig` | `,` | 33080 |
| `order-line-states.csv` | `utf-8-sig` | `,` | 38570 |
| `order-lines.csv` | `utf-8-sig` | `,` | 643280 |
| `orders.csv` | `utf-8-sig` | `,` | 16274 |
| `product-groups.csv` | `utf-8-sig` | `,` | 18 |
| `product-product-group.csv` | `utf-8-sig` | `,` | 5879 |
| `producten.csv` | `utf-8-sig` | `,` | 2581 |
| `quote-lines.csv` | `utf-8-sig` | `,` | 67669 |
| `quote-product-group-details.csv` | `utf-8-sig` | `,` | 31441 |
| `quotes.csv` | `utf-8-sig` | `,` | 23758 |
| `service-orders.csv` | `utf-8-sig` | `,` | 1882 |
| `service_contracts.csv` | `utf-8-sig` | `,` | 128 |
| `suppliers.csv` | `utf-8-sig` | `,` | 33 |
| `wizard-step-logs.csv` | `utf-8-sig` | `,` | 53713 |

## Kolommapping per bestand

### `advisers.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `IntermediaryId` | `intermediaryid` |
| `FirstName` | `firstname` |
| `Insertion` | `insertion` |
| `LastName` | `lastname` |
| `EmailAddress` | `emailaddress` |
| `Phone` | `phone` |

### `customer-lead-information.csv`

| Bronkolom | Doelkolom |
|---|---|
| `CustomerId` | `customerid` |
| `Lead` | `lead` |
| `ExternalId` | `externalid` |

### `customers.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `FirstName` | `firstname` |
| `Insertion` | `insertion` |
| `LastName` | `lastname` |
| `Gender` | `gender` |
| `CompanyName` | `companyname` |
| `EmailAddress` | `emailaddress` |
| `Phone` | `phone` |
| `InvoiceAddressPostCode` | `invoiceaddresspostcode` |
| `InvoiceAddressHouseNumber` | `invoiceaddresshousenumber` |
| `InvoiceAddressHouseNumberExtension` | `invoiceaddresshousenumberextension` |
| `InvoiceAddressStreetName` | `invoiceaddressstreetname` |
| `InvoiceAddressStreetCity` | `invoiceaddressstreetcity` |
| `Language` | `language` |

### `employees.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `FirstName` | `firstname` |
| `Insertion` | `insertion` |
| `LastName` | `lastname` |
| `EmailAddress` | `emailaddress` |
| `Phone` | `phone` |

### `inspections.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `ProductGroupId` | `productgroupid` |
| `InstallationCompanyId` | `installationcompanyid` |
| `PlannedDate` | `planneddate` |
| `PlannedStartFrom` | `plannedstartfrom` |
| `PlannedStartUntil` | `plannedstartuntil` |
| `InspectionNote` | `inspectionnote` |
| `IsFinished` | `isfinished` |

### `installation-requirement-rules.csv`

| Bronkolom | Doelkolom |
|---|---|
| `InstallationRequirementId` | `installationrequirementid` |
| `From` | `from` |
| `To` | `to` |
| `Amount` | `amount` |

### `installation-requirement.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `ForProductId` | `forproductid` |
| `RequiredProductId` | `requiredproductid` |
| `AmountType` | `amounttype` |
| `Amount` | `amount` |

### `installations.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `ProductGroupId` | `productgroupid` |
| `InstallationCompanyId` | `installationcompanyid` |
| `PlannedDate` | `planneddate` |
| `PlannedStartFrom` | `plannedstartfrom` |
| `PlannedStartUntil` | `plannedstartuntil` |
| `InstallationNote` | `installationnote` |
| `IsFinished` | `isfinished` |

### `intermediaries.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `Name` | `name` |
| `IsActive` | `isactive` |
| `PostCode` | `postcode` |
| `HouseNumber` | `housenumber` |
| `HouseNumberExtension` | `housenumberextension` |
| `Street` | `street` |
| `City` | `city` |
| `KvkNumber` | `kvknumber` |
| `Iban` | `iban` |
| `Website` | `website` |
| `VatNumber` | `vatnumber` |
| `Phone` | `phone` |
| `EmailAddress` | `emailaddress` |
| `IsEPAOffice` | `isepaoffice` |
| `PreferredEPAOfficeId` | `preferredepaofficeid` |
| `EmployeeId` | `employeeid` |

### `invoices-lines.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `InvoiceId` | `invoiceid` |
| `Quantity` | `quantity` |
| `Description` | `description` |
| `PricePerUnit` | `priceperunit` |
| `TotalVat` | `totalvat` |
| `VatRate` | `vatrate` |
| `TotalExcludingVat` | `totalexcludingvat` |
| `TotalIncludingVat` | `totalincludingvat` |
| `Type` | `type` |
| `ProductGroupId` | `productgroupid` |

### `invoices.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `ServiceOrderId` | `serviceorderid` |
| `CustomerId` | `customerid` |
| `Number` | `number` |
| `Date` | `date` |
| `ExpirationDate` | `expirationdate` |
| `DateSent` | `datesent` |
| `IsPaid` | `ispaid` |
| `PaidOn` | `paidon` |
| `CustomerName` | `customername` |
| `AddressHouseNumber` | `addresshousenumber` |
| `AddressHouseNumberExtension` | `addresshousenumberextension` |
| `AddressPostCode` | `addresspostcode` |
| `AddressCity` | `addresscity` |
| `AddressStreetName` | `addressstreetname` |
| `CreditInvoiceId` | `creditinvoiceid` |
| `IsCredit` | `iscredit` |
| `OriginalInvoiceId` | `originalinvoiceid` |
| `Type` | `type` |

### `order-event-logs.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `EventTypeName` | `eventtypename` |
| `ExecutedAt` | `executedat` |
| `ProductGroupId` | `productgroupid` |
| `Date` | `date` |
| `StartTimeFrom` | `starttimefrom` |
| `StartTimeUntil` | `starttimeuntil` |

### `order-line-states.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `Sequence` | `sequence` |
| `CreatedOn` | `createdon` |

### `order-lines.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderLineStateId` | `orderlinestateid` |
| `OrderId` | `orderid` |
| `Type` | `type` |
| `Quantity` | `quantity` |
| `PricePerUnit` | `priceperunit` |
| `VatRate` | `vatrate` |
| `PurchasePricePerUnit` | `purchasepriceperunit` |
| `Description` | `description` |
| `ProductId` | `productid` |
| `ProductGroupId` | `productgroupid` |
| `ParentOrderLineId` | `parentorderlineid` |

### `orders.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `CustomerId` | `customerid` |
| `AdviserId` | `adviserid` |
| `FrontOfficeEmployeeId` | `frontofficeemployeeid` |
| `BackOfficeEmployeeId` | `backofficeemployeeid` |
| `AddressPostCode` | `addresspostcode` |
| `AddressHouseNumber` | `addresshousenumber` |
| `AddressHouseNumberExtension` | `addresshousenumberextension` |
| `AddressStreetName` | `addressstreetname` |
| `AddressCity` | `addresscity` |
| `OrderStatus` | `orderstatus` |
| `CurrentWizardStep` | `currentwizardstep` |
| `OrderType` | `ordertype` |
| `FoundThrough` | `foundthrough` |
| `HomeAppointmentDate` | `homeappointmentdate` |
| `HomeAppointmentEmployeeId` | `homeappointmentemployeeid` |
| `IsLost` | `islost` |
| `LoseReason` | `losereason` |
| `LoseReasonRemark` | `losereasonremark` |
| `OnHold` | `onhold` |
| `OnHoldReason` | `onholdreason` |
| `HasValidBag` | `hasvalidbag` |
| `CreationDate` | `creationdate` |

### `product-groups.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `Name` | `name` |
| `IsActive` | `isactive` |

### `product-product-group.csv`

| Bronkolom | Doelkolom |
|---|---|
| `ProductId` | `productid` |
| `ProductGroupId` | `productgroupid` |

### `producten.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `Name` | `name` |
| `IsActive` | `isactive` |
| `IsDeleted` | `isdeleted` |
| `Type` | `type` |
| `SupplierId` | `supplierid` |
| `SupplierProductCode` | `supplierproductcode` |
| `EanCode` | `eancode` |
| `ReportingCode` | `reportingcode` |
| `SubsidyAmount` | `subsidyamount` |
| `Description` | `description` |
| `DetailedDescription` | `detaileddescription` |
| `SubsidyConditions` | `subsidyconditions` |
| `ImageFileName` | `imagefilename` |

### `quote-lines.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `QuoteId` | `quoteid` |
| `Quantity` | `quantity` |
| `Price` | `price` |
| `PurchasePrice` | `purchaseprice` |
| `ProductId` | `productid` |
| `OrderLineId` | `orderlineid` |

### `quote-product-group-details.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `QuoteId` | `quoteid` |
| `ProductGroupId` | `productgroupid` |
| `SetPriceExcludingVat` | `setpriceexcludingvat` |
| `SetPriceVat` | `setpricevat` |
| `SetPriceIncludingVat` | `setpriceincludingvat` |
| `ExtraWorkExcludingVat` | `extraworkexcludingvat` |
| `ExtraWorkVat` | `extraworkvat` |
| `ExtraWorkIncludingVat` | `extraworkincludingvat` |
| `ManualDiscountExcludingVat` | `manualdiscountexcludingvat` |
| `ManualDiscountVat` | `manualdiscountvat` |
| `ManualDiscountIncludingVat` | `manualdiscountincludingvat` |
| `IntermediaryDiscountExcludingVat` | `intermediarydiscountexcludingvat` |
| `IntermediaryDiscountVat` | `intermediarydiscountvat` |
| `IntermediaryDiscountIncludingVat` | `intermediarydiscountincludingvat` |
| `TotalDiscountExcludingVat` | `totaldiscountexcludingvat` |
| `TotalDiscountVat` | `totaldiscountvat` |
| `TotalDiscountIncludingVat` | `totaldiscountincludingvat` |
| `IntermediaryAdviceFeeExcludingVat` | `intermediaryadvicefeeexcludingvat` |
| `IntermediaryAdviceFeeVat` | `intermediaryadvicefeevat` |
| `IntermediaryAdviceFeeIncludingVat` | `intermediaryadvicefeeincludingvat` |
| `TotalPriceExcludingVat` | `totalpriceexcludingvat` |
| `TotalPriceVat` | `totalpricevat` |
| `TotalPriceIncludingVat` | `totalpriceincludingvat` |
| `VatRate` | `vatrate` |

### `quotes.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `CreatedOn` | `createdon` |
| `ValidUntil` | `validuntil` |
| `TotalVat` | `totalvat` |
| `TotalExcludingVat` | `totalexcludingvat` |
| `TotalIncludingVat` | `totalincludingvat` |
| `IsApproved` | `isapproved` |
| `ApprovedOn` | `approvedon` |
| `IsActive` | `isactive` |
| `QuoteType` | `quotetype` |
| `OrderLineStateId` | `orderlinestateid` |

### `service-orders.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `OrderId` | `orderid` |
| `CustomerId` | `customerid` |
| `Date` | `date` |
| `StartTimeFrom` | `starttimefrom` |
| `StartTimeUntil` | `starttimeuntil` |
| `IsCancelled` | `iscancelled` |
| `IsCompleted` | `iscompleted` |
| `CompletedAt` | `completedat` |
| `CurrentWizardStep` | `currentwizardstep` |

### `service_contracts.csv`

| Bronkolom | Doelkolom |
|---|---|
| `CustomerId` | `customerid` |
| `DocumentFileName` | `documentfilename` |
| `StartDate` | `startdate` |
| `EndDate` | `enddate` |

### `suppliers.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `Name` | `name` |
| `Phone` | `phone` |
| `EmailAddress` | `emailaddress` |
| `IsActive` | `isactive` |
| `AddressPostCode` | `addresspostcode` |
| `AddressHouseNumber` | `addresshousenumber` |
| `AddressHouseNumberExtension` | `addresshousenumberextension` |
| `AddressStreetName` | `addressstreetname` |
| `AddressCity` | `addresscity` |

### `wizard-step-logs.csv`

| Bronkolom | Doelkolom |
|---|---|
| `Id` | `id` |
| `ExecutionDateTime` | `executiondatetime` |
| `EmployeeId` | `employeeid` |
| `ExecutedStepId` | `executedstepid` |
| `ExecutedStepName` | `executedstepname` |
| `OrderId` | `orderid` |
| `ServiceOrderId` | `serviceorderid` |

