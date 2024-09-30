from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate
from exchange_catalogue_52.schemas.isotc211.org.pkg_19115.pkg_minus_3.gco.pkg_1.pkg_0.base_types import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.iho.int/s100/se/5.2"


class DataStatus(Enum):
    """
    The state of data when a digital signature is created.

    :cvar UNENCRYPTED: The data is unencrypted and uncompressed
    :cvar COMPRESSED: The data is compressed only
    :cvar ENCRYPTED: The data is compressed and encrypted
    """
    UNENCRYPTED = "unencrypted"
    COMPRESSED = "compressed"
    ENCRYPTED = "encrypted"


@dataclass
class DatasetPermitType:
    """
    Permit record element (S-100 15-7.4.4).

    :ivar filename: The file name as defined in
        S100_DatasetDiscoveryMetadata – fileName. It enables Data Client
        systems to link the correct encryption key to the corresponding
        encrypted file. The pathName to the file is defined in the
        Exchange Set Metadata
    :ivar edition_number: The edition number of the product file as
        defined in S100_DatasetDiscoveryMetadata  - editionNumber. For
        products without an edition number the permit will apply to all
        issued datasets.
    :ivar issue_date: If the product does not have an edition number
        then the issue date may be used as an alternative identifier
    :ivar expiry: This is the date when the Data Clients licence
        expires. Systems must prevent any new editions or updates issued
        after this date from being installed
    :ivar encrypted_key: EK contains the decryption key for the
        specified edition of the product file
    """
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )
    edition_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "editionNumber",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
        }
    )
    expiry: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
        }
    )
    encrypted_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "encryptedKey",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )


@dataclass
class PermitHeaderType:
    """
    File creation date, the name of the Data Server and the format version.

    :ivar issue_date: Date and time
    :ivar data_server_name: Name of Data Server who has generated the
        permit file. The Data Server name should be consistent and use
        the same organizational contact as defined in
        S100_ExchangeCatalogue – contact
    :ivar data_server_identifier: Short identifier of data server
    :ivar version: Version number of S-100. It will be compatible with
        the IHO version numbering scheme X.Y.Z.
    :ivar userpermit: The user permit that the permit is intended for.
        This allows the client system or implementer to validate the
        destination. The end-user system must be capable of checking if
        the permit is for the designated system on a multi system
        bridge.
    """
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )
    data_server_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataServerName",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )
    data_server_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataServerIdentifier",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )
    userpermit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )


@dataclass
class S100SeCertificateType:
    """
    For embedding in files that contains signatures e.g exchange set catalogues or
    standalone signature file.

    :ivar value:
    :ivar id: Each XML element containing a certificate will have a
        unique identifier attribute “id”.
    :ivar issuer: Each XML certificate definition will also include an
        attribute, “issuer” defining the id of the issuer, either the SA
        (identified by the schemeAdministrator id) or a domain
        coordinator (whose certificate will also be included in the
        Exchange Set).
    """
    class Meta:
        name = "S100_SE_CertificateType"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    issuer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class S100SeDigitalSignature:
    """Type contains the signature value, an identifier and a reference to the
    certificate that contains the public key.

    The value is an base64 encoded ASN.1
    Dss-Sig-Value  ::=  SEQUENCE  {
    r       INTEGER,
    s       INTEGER  }

    :ivar value:
    :ivar id: Identifier of the digital signature
    :ivar certificate_ref: Signed Public Key
    """
    class Meta:
        name = "S100_SE_DigitalSignature"
        namespace = "http://www.iho.int/s100/se/5.2"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    certificate_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "certificateRef",
            "type": "Attribute",
            "required": True,
        }
    )


class S100SeDigitalSignatureReference(Enum):
    """A reference to a cryptographic algorithm used in an implementation of Part
    15 Only DSA is currently used in implementations of S-100 for file based
    transfer of data to ECDIS.

    Other values are included for interoperability with other
    implementations by external standards. See clause 15-8.4

    :cvar RSA: RSA with key length &gt;= 2048 bits
    :cvar DSA: DSA with key length &gt;= 2048 bits
    :cvar ECDSA: ECDSA with key length &gt;= 224 bits
    :cvar ECDSA_224_SHA2_224: 224 bits ECDSA with SHA2-224 hashing
    :cvar ECDSA_224_SHA3_224: 224 bits ECDSA with SHA3-224 hashing
    :cvar ECDSA_256_SHA2_256: 256 bits ECDSA: SHA2-256
    :cvar ECDSA_256_SHA3_256: 256 bits ECDSA: SHA3-256
    :cvar ECDSA_384_SHA2: 384 bits ECDSA: SHA2-384
    :cvar ECDSA_384_SHA3: 384 bits ECDSA: SHA3-384
    :cvar AES_128: AES 128 bit keys
    :cvar AES_192: AES 192 bit keys
    :cvar AES_256: AES 256 bit keys
    """
    RSA = "RSA"
    DSA = "DSA"
    ECDSA = "ECDSA"
    ECDSA_224_SHA2_224 = "ECDSA-224-SHA2-224"
    ECDSA_224_SHA3_224 = "ECDSA-224-SHA3-224"
    ECDSA_256_SHA2_256 = "ECDSA-256-SHA2-256"
    ECDSA_256_SHA3_256 = "ECDSA-256-SHA3-256"
    ECDSA_384_SHA2 = "ECDSA-384-SHA2"
    ECDSA_384_SHA3 = "ECDSA-384-SHA3"
    AES_128 = "AES-128"
    AES_192 = "AES-192"
    AES_256 = "AES-256"


@dataclass
class ProductsPermitType:
    """
    Permits from the Data Server for the specified product.

    :ivar product: The header element in the PERMIT.XML file is followed
        by a single element called “products” which contains multiple
        “product” records, each of which contain the actual permits for
        those products (S-100 15-7.4.3).
    """
    product: List["ProductsPermitType.Product"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Product:
        """
        :ivar dataset_permit: Permit record element
        :ivar id: The attribute “id” for each product section contains
            the S-100 identifier of the Product Specification to which
            the permits relate (S-100 15-7.4.3).
        """
        dataset_permit: List[DatasetPermitType] = field(
            default_factory=list,
            metadata={
                "name": "datasetPermit",
                "type": "Element",
                "namespace": "http://www.iho.int/s100/se/5.2",
                "min_occurs": 1,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class S100SeCertificateContainerType:
    """
    A set of signed public key certificates.

    :ivar scheme_administrator: The scheme administrator identity.
    :ivar certificate: A signed public key certificate
    """
    class Meta:
        name = "S100_SE_CertificateContainerType"

    scheme_administrator: Optional["S100SeCertificateContainerType.SchemeAdministrator"] = field(
        default=None,
        metadata={
            "name": "schemeAdministrator",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "required": True,
        }
    )
    certificate: List[S100SeCertificateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "min_occurs": 1,
        }
    )

    @dataclass
    class SchemeAdministrator:
        """
        :ivar id: The identity of the Scheme Administrator is contained
            in the id attribute of the schemeAdminstrator element.
        """
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class S100SeDigitalSignatureReferencePropertyType:
    """
    Property type for S100_SE_DigitalSignatureReference.
    """
    class Meta:
        name = "S100_SE_DigitalSignatureReference_PropertyType"

    value: Optional[S100SeDigitalSignatureReference] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class S100SeDigitalSignaturePropertyType(S100SeDigitalSignature):
    """
    Property type for S100_SE_DigitalSignature.
    """
    class Meta:
        name = "S100_SE_DigitalSignature_PropertyType"

    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://standards.iso.org/iso/19115/-3/gco/1.0",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class S100SeSignatureOnData(S100SeDigitalSignature):
    """
    :ivar data_status: For data signatures only] whether the signature
        is of an unencrypted resource, one which is compressed only
        (such as an archive of multiple resources) or encrypted (and
        compressed)
    """
    class Meta:
        name = "S100_SE_SignatureOnData"
        namespace = "http://www.iho.int/s100/se/5.2"

    data_status: Optional[DataStatus] = field(
        default=None,
        metadata={
            "name": "dataStatus",
            "type": "Attribute",
        }
    )


@dataclass
class S100SeSignatureOnSignature(S100SeDigitalSignature):
    """
    :ivar signature_ref: The digital signature referenced
    """
    class Meta:
        name = "S100_SE_SignatureOnSignature"
        namespace = "http://www.iho.int/s100/se/5.2"

    signature_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "signatureRef",
            "type": "Attribute",
        }
    )


@dataclass
class PermitType:
    """
    The root element of the permit file.

    :ivar header: File creation date, the name of the Data Server and
        the format version
    :ivar products: Permits from the Data Server for the specified
        product
    """
    header: List[PermitHeaderType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "min_occurs": 1,
            "sequence": 1,
        }
    )
    products: List[ProductsPermitType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
            "min_occurs": 1,
            "sequence": 1,
        }
    )


@dataclass
class S100SeAdditionalSignature:
    """
    Elements of this type can be used within the dataset discovery metadata
    elements of an exchanges set catalogue.

    :ivar signature_on_signature: Unique identifier of the digital
        signature value
    :ivar signature_on_data: The public key which the signature can be
        verified against. This is only optional if the signed public key
        is included in a digital signature element itself, otherwise it
        is mandatory
    """
    class Meta:
        name = "S100_SE_AdditionalSignature"

    signature_on_signature: Optional[S100SeSignatureOnSignature] = field(
        default=None,
        metadata={
            "name": "signatureOnSignature",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
        }
    )
    signature_on_data: Optional[S100SeSignatureOnData] = field(
        default=None,
        metadata={
            "name": "signatureOnData",
            "type": "Element",
            "namespace": "http://www.iho.int/s100/se/5.2",
        }
    )


@dataclass
class StandaloneDigitalSignature:
    """
    The root elements for CATALOG.SIGN or PERMIT.SIGN.

    :ivar filename: The filename of the content signed
    :ivar certificates: Any certificates required to authenticate the
        signature against the SchemeAdministrator
    :ivar s100_se_signature_on_data:
    :ivar s100_se_signature_on_signature:
    :ivar digital_signature: A single digital signature
    """
    class Meta:
        namespace = "http://www.iho.int/s100/se/5.2"

    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    certificates: Optional[S100SeCertificateContainerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    s100_se_signature_on_data: Optional[S100SeSignatureOnData] = field(
        default=None,
        metadata={
            "name": "S100_SE_SignatureOnData",
            "type": "Element",
        }
    )
    s100_se_signature_on_signature: Optional[S100SeSignatureOnSignature] = field(
        default=None,
        metadata={
            "name": "S100_SE_SignatureOnSignature",
            "type": "Element",
        }
    )
    digital_signature: Optional[S100SeDigitalSignature] = field(
        default=None,
        metadata={
            "name": "digitalSignature",
            "type": "Element",
        }
    )


@dataclass
class Permit(PermitType):
    """
    The root element of the permit file.
    """
    class Meta:
        namespace = "http://www.iho.int/s100/se/5.2"
